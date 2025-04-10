def is_in_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False

def main():
    try:
        num = int(input("Enter a number: "))
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    if is_in_range(num, start, end):
        print(f"{num} is within the range of {start} and {end}.")
    else:
        print(f"{num} is not within the range of {start} and {end}.")

if __name__ == "__main__":
    main()