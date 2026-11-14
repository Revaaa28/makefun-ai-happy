"""ai-happy-01 entry: copies the committed entry.png to the output directory.

The grader runs this in a fresh container with /output writable;
outside the container, MAKEFUN_OUTPUT_DIR stands in for /output.
Python 3.13, standard library only.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"entry image missing beside main.py: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    print(f"entry.png written to {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
