#[allow(unused_imports)]
#[allow(unused_allocation)]
#[allow(unused_variables)]
use std::io::{self, Write};
use std::process::Command;

fn main() {

    // Wait for user input
    let stdin = io::stdin();
    let mut stdout = io::stdout();    
    let mut input = String::new();
    loop{
        print!("$ ");
        stdout.flush().unwrap();
        stdin.read_line(&mut input).unwrap();
        input.pop();

        let args: Vec<&str> = input.trim().split_whitespace().collect();
        if args.is_empty(){
            continue;
        }

        match args[0]{
            
            //exit
            "exit" => {
                if args.len() == 2 && args[1] == "0"{
                    break;
                }
                else {
                    println!("{}: command not found",input.trim());
                }
            },
        
            //echo 
            "echo" => {
                let message = args[1..].join(" ");
                println!("{}",message);
            },

            //help 
            "help" => {
                println!("help");
            },
            
            //Deepai 
            "deepai" => {
                if args.len() < 3 {
                    println!("Prompt error\n");
                    println!("Usage:\n1.deepai <input_file> --modify\n2.deepai <input_file> --newfile <output_file>");
                    continue;
                }
                let input_file = args[1];
                let output_file = if args[2] == "--modify" {
                    input_file
                } else if args[2] == "--newfile" && args.len() == 4 {
                    args[3]
                } else {
                    println!("Invalid syntax. Use --modify or --newfile <output_file>");
                    continue;             
                };

                let status = Command::new("python3")
                    .arg("/home/Prithiv/codes/rust/deepvibe/scripts/script.py")
                    .arg(input_file)
                    .arg(output_file)
                    .status()
                    .expect("Failed to execute script");

                if status.success(){
                    println!("Processing complete: {}",output_file);
                }
                else {
                    println!("Error running script");
                }
            },
            _ => println!("{}: command not found",input.trim()),

        }
        input.clear();
    }
}
