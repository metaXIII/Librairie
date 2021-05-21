fn distance_2d(x1: i32, x2:i32, y1:i32, y2:i32) ->f64 {
    let distance:f64 = (((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) as f64).sqrt();
    return distance;
}

fn main() {
    println!("{}",distance_2d(3, 3, 3 , 3))
        
}