import shutil
from pathlib import Path

current_folder = Path().cwd()
# Path.home() eller Path().home() ger oss home folder

copies_folder = current_folder / "copies"

copies_folder.mkdir(exist_ok=True)  # skapar en submapp copies i nuvarande mapp


# shutil.copy kopierar en fil och dess innehåll
shutil.copy(src="test.ini", dst=copies_folder / "test.bak.ini")

# shutil.copy2 kopierar en fil och dess innehåll + metadata
shutil.copy2("test.ini", copies_folder / "test.bak.ini")

# shutil.move flyttar en fil från src till dest
shutil.move("test.bak.ini", copies_folder / "test.bak.ini")


"""
Alternativt sätt att importera shutil
from shutil import copy, copy2, move

copy(src="test.ini", dst=copies_folder / "test_2.bak.ini")
copy2("test.ini", copies_folder / "test_2.bak.ini")
move(src=..., dst=...)
"""
