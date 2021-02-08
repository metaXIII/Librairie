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


# Les méthodes :
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
age = 30
autre_var = []
print(declaration)
print(type(word))
print(type(list))

# Obtenir le type d'une variable : type
print(type(4))
print(type("hello world"))
print(type(["aze", "aze2"]))


# D'autres types de données

## Tuples
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

## Les listes
list = []
list.append("something")

print(list)
print()

# Boucles :

for item in list:
    print(item)
list = [0,3,4,2,1]
for item in list:
    print(item)
list.sort()
for item in list:
    print(item)


print()
print("Fin du programme")
