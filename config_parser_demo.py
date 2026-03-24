import configparser
import shutil

"""
Syntax för att skriva ut från en dictionary. Jämför denna med
configparsers syntax så ser ni att det är likt

conf_dict_nestled = {"network": {"hostname": "localhost", "ip": 1}}
print(conf_dict_nestled)
print(conf_dict_nestled["network"]["hostname"])
print(conf_dict_nestled["network"]["ip"])
print(conf_dict_nestled.get("network", {}).get("ip", "fallback value"))
"""


# objekt av typen ConfigParser
config = configparser.ConfigParser()


# with open()... så brukar vi läsa in textfiler
# text = f.read()

# med configparser läser vi in till själva config-objektet direkt
# ingenting sparas till en ny variabel utan config innehåller nu infon
config.read("test.ini")

print("Config file (unreadable for us humans):", config)

for key, value in config["databas"].items():
    print(key, value)


# get-syntaxen är den som är bäst för att läsa
# get = sträng implicit
# getint = heltal
# getfloat = flyttal
# getboolean = boolean
print("Utvalt värde:", config["databas"]["password"])
print(
    "Utvalt värde med get-syntax:",
    config.get("databas", "password", fallback=None),
)

# Set-syntax = ändra på värde, eller skapa nytt
# set-syntax är den bästa

# config["databas"]["password"] = "new password"
config.set(section="databas", option="password", value="New value of password")


print("Ändrat värde:", config["databas"]["password"])

"""
Vi måste säkerhetskopiera filen innan vi gör en ändring.
med shutil.copy2()
"""

shutil.copy2("test.ini", "test.bak.ini")

"""
Jag vill nu spara mitt ändrade värde i ini-filen
Detta gör jag med with open men jag skriver med min config.
config.write(configfile). Denna syntax är viktig
"""

# lägg till en ny sektion
# värdet debug = true måste vara strängar
config["New Section"] = {"debug": "true"}

# alternativt sätt:
config.set("New Section", "another_debug", "true")


with open("test.ini", "w") as configfile:
    config.write(configfile)
