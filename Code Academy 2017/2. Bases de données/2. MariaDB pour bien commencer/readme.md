# MariaDB

## Installation MariaDB

MariaDB est un fork de MySQL.
Utiliser le package manager sous linux pour récupérer les sources.
Installez ensuite la base de données sur votre poste avec la commande.


```
    sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

Démarrez le service : 

```
    sudo systemctl start mysqld
```

N'hésitez pas à initialiser les services pour qu'ils démarrent directement au démarrage.

```
    sudo systemctl enable mysqld
```


## Se connecter

```
    sudo mysql -uroot
```
(par défaut, mysql n'a pas de mot de passe, vous pouvez ensuite modifier cet état en faisant quelques recherches)


### Recommandations: 

Pour travailler avec les bases de données, il est préférables d'attribuer les droits à un utilisateur pour une tache précise et donc ne pas utiliser root en permanence.


# Dumps des bases de données :

```
    mysqldump [nom de la base de données] [nom de la table] -u root -p > save.sql
```
Cette commande permet de récupérer une table d'une base de données dans un fichier (save.sql ici)
Dans ce cas, la table sera exporté sans la commande de création de la base de données.
Si vous souhaitez exporter une database entière, vous pouvez utiliser : 
```
    mysqldump -B [nom de la base de données] -u root -p > save.sql
```



## Insertion depuis un fichier

```
    mysql [nom de la base de données] -u root -p < save.sql
```
Cette commande permet d'insérer depuis un fichier des données dans la base de données.