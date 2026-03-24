"""
dictionary

datastruktur med kvp (key value pair)

my_dict = {"key":"value"}
    - vi har nyckel som sträng eller heltal (enklast så)
    - value kan vara vad som helst. int, str, bool, dict, list etc
    - en nyckel måste vara unik
"""

# string eller in som nyckeltyp
my_dict = {
    "key": "value",
    "section": {"hostname": "localhost", "port": 1},
    "lista": [1, 2, 3, 4, 5],
}

# vi kan skriva ut värdet med ["key name"]
# print(my_dict["key"])
# print("Nästlat: ", my_dict["section"]["hostname"])
# print("key: lista", my_dict["lista"])

# print(my_dict["nyckeln finns inte"])
# bättre sätt
# res = my_dict.get("Finns inte", "Standardvärde/Unknown")
# print(res)

# my_dict["ny nyckel"] = "Nytt värde"
# print(my_dict)

# dictionaries har kvp = key value pair
# nyckel är unik!


# OOP = klasser

from pathlib import Path

heltal = 1
sträng = "A"
current_folder = Path.cwd()

# Path är en klass skapad av Python
# Den ska motsvara sökvägar

print(current_folder.parts) # attribut
print(current_folder.stem) # attribut
current_folder.cwd() # metod/funktion
# finns inte för heltal/strängar
# sträng.cwd()
# heltal.cwd()