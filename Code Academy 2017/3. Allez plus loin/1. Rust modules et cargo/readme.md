# Installation de rust

```
curl -sSf https://sh.rustup.rs | sh
```

## Hello world

Création d'un fichier hello.rs

Ouvrir ce fichier et y inscrire : 

```
println!("Hello world");
```

compiler le fichier avec la commande :
```
rustc hello.rs
```

Lancement du fichier avec 
```
./hello
```

## Utilisation du framework cargo

### Création d'un nouveau helloworld avec cargo 
```
cargo new helloWorld --bin
```

### Compiler le projet : 

Il faut aller dans le projet à la racine et lancer la commande :
```
cargo build
```

Run du projet : 
```
cargo run
```

clean du projet : 
```
cargo clean
```