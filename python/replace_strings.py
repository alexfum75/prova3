from pathlib import Path

SOSTITUZIONI = {
    "Perche'": "Perché",
    "perche'": "perché",
    "E'": "È",
    "caffe'": "caffè",
    "universita'": "università",
    "a'": "à",
    "e'": "è",
    "ne'": "né",
    "se'": "sé"
}

print("Working on qmd files")
for path in Path(".").rglob("*.qmd"):
    content = path.read_text(encoding="utf-8")
    modificato = False
    
    # Cicla sulla mappa ed esegue le sostituzioni
    for old_string, new_string in SOSTITUZIONI.items():
        if old_string in content:
            content = content.replace(old_string, new_string)
            print(f"Replaced '{old_string}' with '{new_string}' in: {path}")
            modificato = True
            
    if modificato:
        path.write_text(content, encoding="utf-8")

print("\nWorking on yml files")
for path in Path(".").rglob("_quarto.yml"):
    content = path.read_text(encoding="utf-8")
    modificato = False
    
    # Cicla sulla mappa ed esegue le sostituzioni
    for old_string, new_string in SOSTITUZIONI.items():
        if old_string in content:
            content = content.replace(old_string, new_string)
            print(f"Replaced '{old_string}' with '{new_string}' in: {path}")
            modificato = True
            
    if modificato:
        path.write_text(content, encoding="utf-8")
