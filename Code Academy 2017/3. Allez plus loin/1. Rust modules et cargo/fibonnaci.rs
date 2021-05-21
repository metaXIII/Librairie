fn fibonnaci(n: i32) ->i32 {
    if n == 0 {
        return 0;
    }
    if n <= 1 {
        return 1;
    }
    else {
        return fibonnaci(n - 1) + fibonnaci(n - 2);
    }
}

fn main() {
    for x in 0..10 {
        println!("Fibonnaci number {} is {}", x, fibonnaci(x))
    }
}