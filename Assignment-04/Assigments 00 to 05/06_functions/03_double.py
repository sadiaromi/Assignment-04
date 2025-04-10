def double(num):
    return num * 2 

def main():
    while True:
        user_input = input("Enter a number to double (or type 'exit' to quit): ")

        if user_input.lower() == "exit":  
            print("Exiting the program. Goodbye! 👋")
            break 

        try:
            num = int(user_input)  
            result = double(num)
            print(f"Double of {num} is {result}\n")
        except ValueError:  
            print("Invalid input! Please enter a valid integer or type 'exit' to quit.\n")

main()