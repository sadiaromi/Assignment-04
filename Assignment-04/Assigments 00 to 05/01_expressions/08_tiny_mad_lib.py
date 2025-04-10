def mad_lib():
    verb: str = str(input("Enter a verb: "))
    adjective: str = str(input("Enter an adjective: "))
    noun: str = str(input("Enter a noun: "))

    print(f"Do you {verb} your {adjective} {noun}?")

if __name__ == '__main__':
    mad_lib()