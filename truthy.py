string = "" # tom textsträng är Falsy != False
string = "A" # icke-tom textsträng är truthy

if bool(string) == True:
    print("True?")
else:
    print("False?")
