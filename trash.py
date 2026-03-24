# kräver pip och helst en venv
# venv skickas aldrig med till git/github
import send2trash
from pathlib import Path

# skicka alla filer i nuvarande mapp som slutar på .ini till papperskorgen
for file in Path.cwd().glob("*.ini"):
    if input(f"Vill du radera filen ({file.name})? (y/n): ") == "y":
        send2trash.send2trash(file)
