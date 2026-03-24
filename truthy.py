string = ""  # tom textsträng är Falsy != False

if string:
    print("Is this printed?")

string = "A"  # icke-tom textsträng är truthy

if string:
    print("Is this printed?")


# Python gör en bool()-konvertering implicit när man skriver if value och value inte är en boolean
if bool(string) == True:
    print("True?")
else:
    print("False?")
