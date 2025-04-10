MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        print(last_element)


def get_lst():
    lst = []
    elem = input("Enter an element of the list: ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element of the list: ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()