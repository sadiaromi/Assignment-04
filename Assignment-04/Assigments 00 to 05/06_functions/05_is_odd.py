
def is_odd(number):
    return number % 2 != 0

def main():
    try:
        num = int(input("Enter a number to check if it's odd: "))
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")
        return

    if is_odd(num):
        print(f"✅ {num} is an odd number.")
    else:
        print(f"❌ {num} is not an odd number (it's even).")

if __name__ == "__main__": 
    main()
