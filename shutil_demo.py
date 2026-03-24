import shutil
from pathlib import Path

current_folder = Path().cwd()
# Path.home() eller Path().home()

copies_folder = current_folder / "copies"

copies_folder.mkdir(exist_ok=True)



shutil.copy(src="test.ini", dst=copies_folder / "test.bak.ini")
shutil.copy2("test.ini", copies_folder / "test.bak.ini")
shutil.move("test.bak.ini", copies_folder / "test.bak.ini")

from shutil import copy, copy2, move

copy(src="test.ini", dst=copies_folder / "test_2.bak.ini")
copy2("test.ini", copies_folder / "test_2.bak.ini")
# move()