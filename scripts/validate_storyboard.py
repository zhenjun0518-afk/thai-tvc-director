#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED_SHOT_FIELDS = [
    "shot_id", "start", "end", "story_function", "action", "product_state", "continuity_notes"
]


def main():
    ap = argparse.ArgumentParser(description="Validate Thai TVC storyboard JSON")
    ap.add_argument("storyboard_json")
    ap.add_argument("--duration", type=float, required=True)
    args = ap.parse_args()
    data = json.loads(Path(args.storyboard_json).read_text(encoding="utf-8"))
    shots = data.get("shots", data if isinstance(data, list) else [])
    errors = []

    if not shots:
        errors.append("no shots")
    ids = set()
    prev_end = 0.0
    for i, shot in enumerate(shots):
        for f in REQUIRED_SHOT_FIELDS:
            if f not in shot:
                errors.append(f"shot {i+1} missing {f}")
        sid = shot.get("shot_id")
        if sid in ids:
            errors.append(f"duplicate shot_id: {sid}")
        ids.add(sid)
        try:
            start = float(shot.get("start"))
            end = float(shot.get("end"))
            if end <= start:
                errors.append(f"{sid}: end <= start")
            if start + 0.05 < prev_end:
                errors.append(f"{sid}: overlaps previous shot")
            prev_end = max(prev_end, end)
        except Exception:
            errors.append(f"{sid}: invalid start/end")

    if shots:
        final_end = float(shots[-1].get("end", 0))
        if abs(final_end - args.duration) > max(1.0, args.duration * 0.05):
            errors.append(f"final end {final_end}s differs from target {args.duration}s")

    if errors:
        for e in errors:
            print("[FAIL]", e)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
