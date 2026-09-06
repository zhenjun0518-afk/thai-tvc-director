#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED = [
    "product_name",
    "core_selling_point",
    "human_insight",
    "story_mode",
    "one_line_idea",
    "hook",
    "escalation",
    "twist",
    "product_role",
    "packshot",
]


def main():
    ap = argparse.ArgumentParser(description="Validate Thai TVC story JSON")
    ap.add_argument("story_json")
    args = ap.parse_args()
    data = json.loads(Path(args.story_json).read_text(encoding="utf-8"))
    errors = []
    for key in REQUIRED:
        if not str(data.get(key, "")).strip():
            errors.append(f"missing/empty: {key}")

    if data.get("product_removal_story_still_works") is True:
        errors.append("product causality failed: story still works after removing product")

    claims = data.get("unverified_claims", [])
    if claims:
        errors.append("unverified_claims must be empty")

    score = data.get("quality_score")
    if score is not None and score < 80:
        errors.append("quality_score must be >= 80")

    if errors:
        for e in errors:
            print("[FAIL]", e)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
