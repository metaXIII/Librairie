fn sum(num: (i32, i32)) -> i32 {
    return num.0 + num.1;
}

fn found_max(pair: (i32, i32)) -> i32 {
    let (a, b) = pair;
    if a > b {
        return a;
    }
    else {
        return b;
    }
}

fn double_int(x:i32) -> i32 {
    return x + x;
}

fn main() {
    let pair = (1, 3);
    println!("current value of pair : {:?}", pair);
    println!("current value of sum : {}", sum(pair));
    println!("current max: {}", found_max(pair));
    let x: fn(i32) -> i32 = double_int;

    for i in 0..10 {
        println!("{} * 2 = {}", i, x(i));
    }
}