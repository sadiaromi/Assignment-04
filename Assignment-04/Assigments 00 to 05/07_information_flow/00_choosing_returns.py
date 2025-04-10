ADULT_AGE = 18

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

def get_age_input():
    while True:
        try:
            age = int(input("How old is this person?: "))  
            if age < 0:
                print("Age can't be negative. Please enter a valid age.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")

def main():
    age = get_age_input()  
    if is_adult(age):
        print(f"Age {age} is considered an adult age. True")
    else:
        print(f"Age {age} is not an adult age. False")

main()