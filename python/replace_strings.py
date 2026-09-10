from pathlib import Path

OLD_STRING = "Perche'"
NEW_STRING = "Perché"

print("Working on qmd files")
for path in Path(".").rglob("*.qmd"):
    content = path.read_text(encoding="utf-8")
    if OLD_STRING in content:
        path.write_text(content.replace(OLD_STRING, NEW_STRING), encoding="utf-8")
        print(f"Replaced {OLD_STRING} in: {path}")

print("Working on yml files")
for path in Path(".").rglob("_quarto.yml"):
    content = path.read_text(encoding="utf-8")
    if OLD_STRING in content:
        path.write_text(content.replace(OLD_STRING, NEW_STRING), encoding="utf-8")
        print(f"Replaced {OLD_STRING} in: {path}")