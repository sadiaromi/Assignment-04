def get_last_element(lst):
    print(lst[-1])

def get_lst():
    lst = []
    elem:str = input("Enter an element of the list: ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element of the list: ")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":
    main()
    