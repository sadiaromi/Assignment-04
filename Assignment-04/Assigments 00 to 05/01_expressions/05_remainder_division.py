def remainder():
    num1: int = int(input("Enter an integer to be divided: "))
    num2: int = int(input("Enter an integer to divide by: "))
    quotient: int = num1 // num2
    remainder: int = num1 % num2
    print(f"The result of this division is {quotient}  with a remainder of {remainder}")

if __name__ == '__main__':
    remainder()