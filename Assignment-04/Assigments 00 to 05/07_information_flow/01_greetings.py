def greet(name):
    return f"Hello {name}, hope you have an amazing day ahead!"

def main():
    name = input("What's your name? ")
    greeting_message = greet(name)
    print(greeting_message)

if __name__ == "__main__":
    main()