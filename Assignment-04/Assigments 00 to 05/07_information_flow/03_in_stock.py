def num_in_stock(fruit, stock):
    return stock.get(fruit.lower(), 0)

def main():
    stock = {
        "apple": 10,
        "banana": 12,
        "orange": 24,
        "mango": 10,
        "grapes": 0
    }

    fruit = input("Enter a fruit: ").strip()

    quantity = num_in_stock(fruit, stock)

    if quantity > 0:
        print(f"This fruit is in stock! Here is how many:\n{quantity}")
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
