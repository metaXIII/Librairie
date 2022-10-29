#!/usr/bin/env python2

integer = input("Combien de nombre entiers ?")
try:
    integer = int(integer)
except ValueError:
    exit("Vous devez saisir un nombre entier")

ints = list()
count = 0

while count < integer:
    number = input("Veuillez saisir le nombre entier {0} svp : \n".format(count + 1))
    isInt = False
    try:
        number = int(number)
        isInt = True
    except ValueError:
        print("Vous devez saisir un nombre entier")
    if isInt:
        ints.append(number)
        count += 1

print("Execution de la boucle for : ")
for value in ints:
    print(value)

print("Execution de la boucle while : ")
i = 0
while i < len(ints):
    print(ints[i])
    i += 1