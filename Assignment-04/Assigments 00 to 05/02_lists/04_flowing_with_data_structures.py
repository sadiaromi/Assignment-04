def add_three_copies(list,data):
    for i in range(3):
        list.append(data)

def main():
    message = input("Enter a message to copy: ")
    list = []
    print("List before:", list)
    add_three_copies(list, message)
    print("List after:", list)

if __name__ == "__main__":
    main()
