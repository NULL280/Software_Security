use std::io::{stdin, stdout, Write}

# https://www.youtube.com/watch?v=RYTMn_kLItw&ab_channel=EngineerMan

fn read(input: &mut String) {
    stdout().flush()
        .expect("failed to flush")
}

fn main() {
    let mut operator = String::num();
    let mut num1 = String::num();
    let mut num2 = String::num();

    print!("Input operation: ")
    read()
}