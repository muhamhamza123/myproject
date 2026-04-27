"""
run_reproducibility.py
End-to-end reproducibility runner for SE1-SE4 notebooks.
"""

import subprocess
import sys
from pathlib import Path

NOTEBOOKS = [
    "notebooks/SE1_data_access.ipynb",
    "notebooks/SE2_data_processing.ipynb",
    "notebooks/SE3_model_train_validate.ipynb",
    "notebooks/SE4_generate_outputs.ipynb",
]

def run_notebook(nb_path):
    path = Path(nb_path)
    if not path.exists():
        print(f"[SKIP] {nb_path} not found — skipping.")
        return True

    print(f"\n{'='*50}")
    print(f"[RUN]  {nb_path}")
    print(f"{'='*50}")

    result = subprocess.run(
        f"jupyter nbconvert --execute --to notebook --inplace "
        f"--ExecutePreprocessor.timeout=600 {nb_path}",
        shell=True
    )

    if result.returncode != 0:
        print(f"[FAIL] {nb_path} failed!")
        return False

    print(f"[OK]   {nb_path} done.")
    return True

def main():
    print("DIWA Reproducibility Runner — SE1 through SE4")
    failures = []

    for nb in NOTEBOOKS:
        success = run_notebook(nb)
        if not success:
            failures.append(nb)

    print(f"\n{'='*50}")
    if failures:
        print(f"[RESULT] {len(failures)} notebook(s) FAILED:")
        for f in failures:
            print(f"  x {f}")
        sys.exit(1)
    else:
        print("[RESULT] All notebooks completed successfully!")

if __name__ == "__main__":
    main()
