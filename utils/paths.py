from __future__ import annotations

from pathlib import Path


def get_root_dir() -> str:
    # Root directory of the project (directory containing this file's parent)
    # utils/paths.py -> utils/ -> project root
    return str(Path(__file__).resolve().parent.parent)
