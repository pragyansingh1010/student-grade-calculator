from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = list(ROOT.glob("*.py")) + list(ROOT.glob("*.html"))
assert files, "no source file found"
assert all(f.stat().st_size > 0 for f in files)
print("Student Grade Calculator smoke check passed")
