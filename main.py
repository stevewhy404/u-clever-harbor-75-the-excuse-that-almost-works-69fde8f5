#!/usr/bin/env python3
"""The Excuse That Almost Works — writes the one-line excuse to /output/entry.txt."""
import os

LINE = "Boss, the boiler died overnight and the engineer can't come till Thursday, so I'm stuck in a freezing flat waiting."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
