# Variables et types de données.
# 4 types possibles :
#     -   Integer
#     -   Float
#     -   Boolean
#     -   String

# Types de données
# List : données dans un ordre spécifique
# Tuple : données immuables dans un ordre spécifique

hello_str = "Hello world"
hello_int = 30
hello_bool = True
hello_tuple = (21, 32)
hello_list = ["Hello", "world"]

# Déclaration d'une liste vide
print(hello_list[0])
hello_list = list()
# Ne fonctionnera pas vu que la liste n'a pas été initialisé
try:
    print(hello_list[0])  # Out of range exception
except IndexError:
    print("Ne peut pas se faire car il n'y a pas d'indice zéro")
