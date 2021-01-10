# coding: utf-8

import sys
import datetime

begin_time = datetime.datetime.now()
print("Hello world !")

# Pas ajouté dans le magazine, je le rajoute pour vérifier la version de python exécutée.
# Normalement, vous devriez avoir la version 2 de python de lancée.
# Idem pour l'encodage. merci les américains
i = 0
while (i < 1000000):
    print(i)
    i += 1

print(datetime.datetime.now() - begin_time)
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
