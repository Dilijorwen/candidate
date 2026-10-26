"""CLI entry point for preprocessing and inference cells in the notebooks."""

import json
from pathlib import Path

_root = Path(__file__).resolve().parent
for _name, _tag in [
    ("preprocessing.ipynb", "passport-runtime"),
    ("analysis.ipynb", "passport-inference"),
]:
    _notebook = json.loads((_root / "code" / _name).read_text(encoding="utf-8"))
    for _index, _cell in enumerate(_notebook["cells"]):
        if _cell["cell_type"] == "code" and _tag in _cell.get("metadata", {}).get("tags", []):
            exec(compile("".join(_cell["source"]), f"{_name}:cell-{_index}", "exec"), globals())

if __name__ == "__main__":
    globals()["main"](root=_root)
