// Déclaration d'une variable


fn main() {
    let el:i8 = 30;
    let an_array = [3.5, 1.0, 2.0];
    println!("{} éléments dans le tableau",an_array.len());
    println!("Tu as {} age", el);
    
    for i in an_array.iter() {
        println!("{}", i);
    }
    

    //Spécification de la taille d'un tableau en entrée
    let tab1:[i8;3] = [30, 31, 18];
    for i in tab1.iter() {
        println!("{}", i);

    }

    //Déclaration boolean
    let fun = true;

    //Déclaration d'un char
    let character = 'a';
}