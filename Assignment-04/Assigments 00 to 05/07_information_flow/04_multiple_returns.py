import math

def analyze_number(number):
    square = number ** 2
    cube = number ** 3
    square_root = math.sqrt(number)

    return square, cube, square_root

def main():
    try:
        num = float(input("Enter a number: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    square, cube, square_root = analyze_number(num)

    print(f"✅ The square of {num} is: {square}")
    print(f"✅ The cube of {num} is: {cube}")
    print(f"✅ The square root of {num} is: {square_root:.2f}")

if __name__ == "__main__":
    main()