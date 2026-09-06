#!/usr/bin/env python3
from pathlib import Path
import sys
import shutil

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "config/preferences.json",
    "spec/thai-tvc-director.skill.md",
    "references/product-analysis.md",
    "references/creative-routing.md",
    "references/thai-ad-storytelling.md",
    "references/production-workflow.md",
    "references/storyboard-workflow.md",
    "references/image-prompt-workflow.md",
    "references/video-prompt-workflow.md",
    "references/product-consistency.md",
    "references/sound-design.md",
    "references/model-adapters.md",
    "references/quality-and-delivery.md",
]


def main():
    print(f"Thai TVC Director setup check\nroot: {ROOT}")
    ok = True
    if sys.version_info < (3, 10):
        print(f"[FAIL] Python 3.10+ required; current={sys.version.split()[0]}")
        ok = False
    else:
        print(f"[PASS] Python {sys.version.split()[0]}")

    for rel in REQUIRED:
        path = ROOT / rel
        if path.exists() and path.stat().st_size > 0:
            print(f"[PASS] {rel}")
        else:
            print(f"[FAIL] missing/empty: {rel}")
            ok = False

    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        print(f"[INFO] ffmpeg available: {ffmpeg}")
    else:
        print("[INFO] ffmpeg not found; prompt/director modes are unaffected.")

    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
