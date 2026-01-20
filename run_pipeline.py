"""
run_pipeline.py

Execute the UIDAI notebook pipeline in a fixed order using nbconvert.

Order:
1. Concat.ipynb
2. TimeBasedUnderstanding.ipynb
3. Age-Group Behaviour.ipynb
4. Anomaly Detection.ipynb
5. GeographicStress.ipynb
6. ADVANCED LAYER.ipynb
"""

from pathlib import Path
import sys

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


NOTEBOOK_ORDER = [
    "Concat.ipynb",
    "TimeBasedUnderstanding.ipynb",
    "Age-Group Behaviour.ipynb",
    "Anomaly Detection.ipynb",
    "GeographicStress.ipynb",
    "ADVANCED LAYER.ipynb",
]


def run_notebook(notebooks_dir: Path, name: str) -> None:
    notebook_path = notebooks_dir / name

    if not notebook_path.exists():
        print(f"ERROR: Notebook not found: {notebook_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Processing {name}...")

    with notebook_path.open("r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

    try:
        ep.preprocess(nb, {"metadata": {"path": str(notebooks_dir)}})
    except Exception as exc:  # noqa: BLE001
        print(
            f"ERROR: Execution failed for notebook {name}.\n"
            f"Reason: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    project_root = Path(__file__).resolve().parent
    notebooks_dir = project_root / "notebooks"

    for nb_name in NOTEBOOK_ORDER:
        run_notebook(notebooks_dir, nb_name)

    print("All notebooks executed successfully.")


if __name__ == "__main__":
    main()

