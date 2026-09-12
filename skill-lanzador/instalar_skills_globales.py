#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
instalar_skills_globales.py - Promueve los sistemas clo_inv_cual y
exp_psicometrico (project-scoped) a skills+agentes GLOBALES de Claude Code
(~/.claude/skills/, ~/.claude/agents/), resolviendo los nombres que chocan
entre ambos sistemas con un sufijo de dominio.

Uso: python instalar_skills_globales.py [--dry-run]
"""
import re
import sys
from pathlib import Path

HOME_SKILLS = Path.home() / ".claude" / "skills"
HOME_AGENTS = Path.home() / ".claude" / "agents"

SISTEMAS = [
    {
        "src": Path(r"C:\Users\uruk6\OneDrive\Documentos\Age_inv\clo_inv_cual"),
        "sufijo": "cs",
        "etiqueta": "clo_inv_cual",
    },
    {
        "src": Path(r"C:\Users\uruk6\OneDrive\Documentos\exp_psicometrico"),
        "sufijo": "psico",
        "etiqueta": "exp_psicometrico",
    },
]

# Nombres de agente que chocan entre los dos sistemas -> se sufijan en AMBOS.
AGENTES_COLISION = {
    "bibliotecario", "bibliotecario-critic", "coder-critic",
    "explorador-critic", "orquestador",
}
# Nombres de skill (frontmatter name:) que chocan -> se sufijan en AMBOS.
SKILLS_COLISION = {"iniciar", "evaluar"}


def leer(ruta):
    return ruta.read_text(encoding="utf-8")


def escribir(ruta, texto, dry):
    if dry:
        print(f"  [dry] escribiria {ruta} ({len(texto)} bytes)")
        return
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8")


def nombre_final(nombre, colision_set, sufijo):
    return f"{nombre}-{sufijo}" if nombre in colision_set else nombre


def reemplazar_nombres(texto, mapa_agentes, mapa_skills):
    """Reemplaza menciones (case-sensitive por variante) de agentes y
    comandos /skill que colisionan, por su version sufijada."""
    for viejo, nuevo in mapa_agentes.items():
        for variante_vieja, variante_nueva in [
            (viejo, nuevo),
            (viejo.capitalize(), nuevo.capitalize()),
            (viejo.upper(), nuevo.upper()),
            ("-".join(w.capitalize() for w in viejo.split("-")),
             "-".join(w.capitalize() for w in nuevo.split("-"))),
        ]:
            texto = re.sub(r"(?<![\w-])" + re.escape(variante_vieja) + r"(?![\w-])",
                            variante_nueva, texto)
    for viejo, nuevo in mapa_skills.items():
        # /evaluar no debe tocar /evaluar-ia ni /evaluar-tal: exigir que despues
        # del nombre venga espacio, backtick, fin de linea o cierre de comillas.
        texto = re.sub(r"/" + re.escape(viejo) + r"(?=[ `\n\"'.,)]|$)",
                        "/" + nuevo, texto)
    return texto


def procesar_agentes(sistema, mapa_agentes, dry):
    src = sistema["src"] / ".claude" / "agents"
    if not src.is_dir():
        return
    for f in sorted(src.glob("*.md")):
        nombre_viejo = f.stem
        nombre_nuevo = mapa_agentes.get(nombre_viejo, nombre_viejo)
        texto = leer(f)
        texto = re.sub(r"^name:\s*" + re.escape(nombre_viejo) + r"\s*$",
                        f"name: {nombre_nuevo}", texto, count=1, flags=re.M)
        texto = reemplazar_nombres(texto, mapa_agentes, {})
        destino = HOME_AGENTS / f"{nombre_nuevo}.md"
        escribir(destino, texto, dry)
        marca = f" (renombrado de {nombre_viejo})" if nombre_nuevo != nombre_viejo else ""
        print(f"  agente: {nombre_nuevo}{marca}")


def referencias_citadas(texto):
    return sorted(set(re.findall(r"\.claude/references/([\w.-]+\.md)", texto)))


def procesar_skills(sistema, mapa_agentes, mapa_skills, dry):
    src = sistema["src"] / ".claude" / "skills"
    refs_src = sistema["src"] / ".claude" / "references"
    for carpeta in sorted(src.iterdir()):
        skill_md = carpeta / "SKILL.md"
        if not skill_md.is_file():
            continue
        texto = leer(skill_md)
        m = re.search(r"^name:\s*(\S+)\s*$", texto, flags=re.M)
        nombre_viejo = m.group(1) if m else carpeta.name
        nombre_nuevo = mapa_skills.get(nombre_viejo, nombre_viejo)

        refs = referencias_citadas(texto)
        texto = texto.replace(".claude/references/", "references/")
        texto = re.sub(r"^name:\s*" + re.escape(nombre_viejo) + r"\s*$",
                        f"name: {nombre_nuevo}", texto, count=1, flags=re.M)
        texto = reemplazar_nombres(texto, mapa_agentes, mapa_skills)

        destino_dir = HOME_SKILLS / nombre_nuevo
        escribir(destino_dir / "SKILL.md", texto, dry)
        for r in refs:
            ruta_ref = refs_src / r
            if ruta_ref.is_file():
                escribir(destino_dir / "references" / r, leer(ruta_ref), dry)
        marca = f" (renombrado de {nombre_viejo})" if nombre_nuevo != nombre_viejo else ""
        refs_txt = f", {len(refs)} referencia(s)" if refs else ""
        print(f"  skill: {nombre_nuevo}{marca}{refs_txt}")


def main():
    dry = "--dry-run" in sys.argv
    for sistema in SISTEMAS:
        print(f"\n{'='*70}\n{sistema['etiqueta']}  (sufijo: -{sistema['sufijo']})\n{'='*70}")
        mapa_agentes = {a: nombre_final(a, AGENTES_COLISION, sistema["sufijo"])
                         for a in AGENTES_COLISION}
        mapa_skills = {s: nombre_final(s, SKILLS_COLISION, sistema["sufijo"])
                        for s in SKILLS_COLISION}
        procesar_agentes(sistema, mapa_agentes, dry)
        procesar_skills(sistema, mapa_agentes, mapa_skills, dry)


if __name__ == "__main__":
    main()
