"""
dictionary är en datastruktur med kvp (key value pair)

my_dict = {"key":"value"}
    - vi har nyckel som sträng eller heltal (enklast så)
    - value kan vara vad som helst. int, str, bool, dict, list etc
    - en nyckel måste vara unik
"""

# string eller int som nyckeltyp är enklast
# key, section och lista är nycklar
my_dict = {
    "key": "value",
    "section": {"hostname": "localhost", "port": 1},
    "lista": [1, 2, 3, 4, 5],
}

# vi kan skriva ut värdet med ["key name"]

print(my_dict["key"])
print("Nästlat: ", my_dict["section"]["hostname"])
print("key: lista", my_dict["lista"])

# print(my_dict["nyckeln finns inte"])
# bättre sätt. get har en fallback om nyckeln inte finns
res = my_dict.get("Finns inte", "Standardvärde/Unknown")
print(res)

# Nästlat = dict inuti en dict
res_nestled = my_dict.get("Finns inte", {}).get("Finns inte heller", "Unknown")
print(res_nestled)
# Första get skickar {} som default, alltså en tom dict


# För att uppdatera eller tilldela nytt värde
# my_dict["ny nyckel"] = "Nytt värde"
# print(my_dict)

"""
OOP och klasser (syntax)
"""

from pathlib import Path  # OOP-sätt att arbeta med sökvägar och filer

heltal = 1
sträng = "A"
current_folder = (
    Path.cwd()
)  # funktion som returnerar ett path-objekt som motsvarar current working directory

# Path är en klass skapad av Python
# Den ska motsvara sökvägar och filer på ett OOP-sätt

# Attribut och funktioner/metoder nås genom dot notation på objekt
# objektet i detta fall är current_folder-variabeln som har datatypen Path (en klass)

# Attribut har inte () i slutet och ska endast innehålla något som beskriver dem
print(current_folder.parts)  # attribut
print(current_folder.stem)  # attribut


# funktioner/metoder har () i slutet och ska göra något
current_folder.cwd()  # metod/funktion


# funktionerna för ett Path-objekt
# finns inte för heltal/strängar
# Detta är en grundprincip för OOP och klasser
# sträng.cwd()
# heltal.cwd()
