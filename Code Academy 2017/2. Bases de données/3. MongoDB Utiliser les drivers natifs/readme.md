# Utilisation de mongodb

## Installation

### Windows

Télécharger mongodb sur le site de [mongodb](https://www.mongodb.com/try/download/community)

### Linux

```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update
sudo apt install mongodb-org
```

## Utilisation de mongodb

mongodb démarre nativement sur le port 27017
Pour démarrer cette partie, vous devez utiliser la commande mongo qui lance le shell de mongodb et inscrite à l'intérieur :

```
use LXF 
for (var i=0; i< 10000 ; i++) { db.sampleData.insert({x:i, y: i/2})}
```

#### Attention, mongo db est sensible à la casse

## Utilisation du script python

lancer la commande 
``
pip install pymongo
``
pour installer le module manquant si nécessaire.
Démarrez ensuite le script avec la commande
```
python connect.py
```

Quelques notions sont abordés mais le cours est obsolète. Voir exemple.

### Crud Method


|Command|Method|
|-------|------|
|find() | Read but return a collection| 
|findOne() | Read but retorn only one object |
|delete_many() |delete|
|insert_one() |insert |
|someData.update_one() | update |

