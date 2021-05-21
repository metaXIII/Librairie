# Redis

## Installation de redis

Lancer la commande
```
sudo apt install redis-server redis-tools
```


Pour lancer le serveur redis, lancer la commande : 
```
sudo /etc/init.d/redis-server start
```
On peut obtenir le port avec la commande :

```
ps aux | grep redis | grep -v grep
```

## Utilisation de redis avec redis-cli

Il est possible d'insérer une données sous forme de clé, il faut taper:

```
set akey "mihalis"
```

Pour récupérer la clé, il faut taper:

```
get akey
```

On peut également insérer des Sets : 
```
sadd aSet 32 21
sadd aSet 21 11
```
Ce qui retournera :
```
smembers aSet
>11
>21
>32
```

On peut également insérer des collections avec lpush ou rpush (gauche ou droite) : 
```
lpush aList "123"
rpush aList "Hello"
```

Ce qui retournera : 
```
lange aList 0 -1
>123
>Hello
```

On peut également insérer des hash : 
```
hmset myHash CC 2000 1
```

Ce qui retournera

```
hgetall myhash
>CC
>2000
>1
```

## Utilisation de redis avec python

Lire script python
