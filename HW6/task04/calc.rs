use std::io::{stdin, stdout, Write};
// https://www.youtube.com/watch?v=RYTMn_kLItw&ab_channel=EngineerMan
fn read(input: &mut String) {
    stdout().flush()
        .expect("failed to flush");
    stdin().read_line(input)
        .expect("fail to read");
}

fn main() {
    loop {
        let mut operator = String::new();
        let mut num1 = String::new();
        let mut num2 = String::new();

        // read operator
        print!("Input operation: ");
        read(&mut operator);
        // 1 operator char
        let operator: char = operator.trim().chars().next().unwrap();

        let operators = String::from("+-*/e");

        if !operators.contains(operator) {
            println!("ubknown operator");
            continue;
        }

        let operator_name = match operator {
            '+' => "addition",
            '-' => "subtraction",
            '*' => "multiplication",
            '/' => "division",
            _ => return
        };

        // read num1
        print!("Number 1: ");
        read(&mut num1);

        // read num2
        print!("Number 2: ");
        read(&mut num2);

        // debug print
        //println!("{} {} {}", operator, num1, num2);


        // string to float
        let num1: f32 = num1.trim().parse().unwrap();
        let num2: f32 = num2.trim().parse().unwrap();


        let result = match operator {
            '+' => num1 + num2,
            '-' => num1 - num2,
            '*' => num1 * num2,
            '/' => num1 / num2,
            _ => panic!("ERROR in operator")
        };

        println!("Requested operation was {} ({}) and the result is: {}", operator_name, operator, result);
    }
}