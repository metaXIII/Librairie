#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Que sont les données :
print(1)  # Les données peuvent être des chiffres
print("aze")  # des chaines de caractères
print(["hello", "world"])  # des listes
print()

# Travail avec les données :
print(1 + 1)  # 2
print("hello " + "world")  # hello world
print("hello" * 2)  # hellohello
print("hello"[0])  # h
print(["hello", "world"][0])  # hello
print()

# Obtenir le type d'une variable : type
print(type(4))
print(type("hello world"))
print(type(["aze", "aze2"]))

# Méthodes des types :
list = ["banana", "cake", "tiffin"]
print(list)
list.append("chicken")
print(list)
list.insert(1, "something new")
print(list)

word = "HELLO"
print(word)
print(word.lower())


# Les variables :
declaration = "une nouvelle variable"
print(declaration)
print(type(word))
print(type(list))

# Tuples
t = {"aze", "aze2"}
print(t)
try:
    t[1] = "aze3"  # Exception
    print(t)
    pass
except Exception as exception:
    print(exception)
    pass

dictionnary = {
    "free": "someone with liberty",
    "linux": "kind of OS"
}
print(dictionnary["linux"])
dictionnary["linux"] = "better than Windows"
print(dictionnary["linux"])

# Boucles :
print()
for item in list:
    print(item)

print()
print("Fin du programme")
