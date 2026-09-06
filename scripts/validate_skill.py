#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
SDF = ROOT / "spec" / "thai-tvc-director.skill.md"

REQUIRED_HEAD = {"name", "description"}
REQUIRED_MODULES = [
    "DZS-SDF-META",
    "DZS-SDF-IO",
    "DZS-SDF-COGNITION",
    "DZS-SDF-TRIGGER",
    "DZS-SDF-EXEC",
    "DZS-SDF-QUALITY",
]


def frontmatter(text: str):
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        raise ValueError("missing YAML frontmatter")
    return yaml.safe_load(m.group(1)) or {}


def module_yaml(text: str, module: str):
    pattern = rf"# \[{re.escape(module)}\]\s*\n---\s*\n(.*?)\n---"
    m = re.search(pattern, text, re.S)
    if not m:
        raise ValueError(f"missing module {module}")
    return yaml.safe_load(m.group(1)) or {}


def main():
    failures = []
    for path in [SKILL, SDF]:
        if not path.exists():
            failures.append(f"missing {path.relative_to(ROOT)}")

    if failures:
        for f in failures:
            print("[FAIL]", f)
        return 1

    skill_text = SKILL.read_text(encoding="utf-8")
    skill_fm = frontmatter(skill_text)
    missing = REQUIRED_HEAD - set(skill_fm)
    if missing:
        failures.append(f"SKILL.md frontmatter missing: {sorted(missing)}")
    if skill_fm.get("name") != "thai-tvc-director":
        failures.append("SKILL.md name must be thai-tvc-director")

    try:
        json.loads((ROOT / "config/preferences.json").read_text(encoding="utf-8"))
    except Exception as e:
        failures.append(f"preferences.json invalid: {e}")

    sdf_text = SDF.read_text(encoding="utf-8")
    sdf_fm = frontmatter(sdf_text)
    if sdf_fm.get("name") != "thai-tvc-director":
        failures.append("SDF frontmatter name mismatch")

    parsed = {}
    for module in REQUIRED_MODULES:
        try:
            parsed[module] = module_yaml(sdf_text, module)
        except Exception as e:
            failures.append(str(e))

    meta = parsed.get("DZS-SDF-META", {})
    if meta:
        if meta.get("skill_id") != sdf_fm.get("name"):
            failures.append("skill_id must equal frontmatter.name")
        if meta.get("profile") != "L2":
            failures.append("expected L2 profile")

    io = parsed.get("DZS-SDF-IO", {})
    params = {p.get("name") for p in io.get("parameters", []) if isinstance(p, dict)}
    for needed in ["product_image", "product_name", "duration_seconds", "output_mode"]:
        if needed not in params:
            failures.append(f"missing IO parameter: {needed}")

    exec_mod = parsed.get("DZS-SDF-EXEC", {})
    steps = exec_mod.get("execution_plan", []) if isinstance(exec_mod, dict) else []
    ids = {s.get("id") for s in steps if isinstance(s, dict)}
    for s in steps:
        nxt = s.get("on_success")
        if nxt and nxt not in ids and nxt != "terminate_with_success":
            failures.append(f"step {s.get('id')} has unknown on_success={nxt}")

    if failures:
        for f in failures:
            print("[FAIL]", f)
        print("FAIL")
        return 1

    print("[PASS] SKILL frontmatter")
    print("[PASS] preferences JSON")
    print("[PASS] DZS-SDF modules")
    print("[PASS] skill_id/frontmatter match")
    print("[PASS] execution graph references")
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
