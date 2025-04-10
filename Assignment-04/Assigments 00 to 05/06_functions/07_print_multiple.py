def print_multiple(message, repeats):
    for _ in range(repeats):  
        print(message)  

def main():
    message = input("Enter a message: ") 
    repeats = int(input("How many times to repeat?: ")) 
    print_multiple(message, repeats)

main()