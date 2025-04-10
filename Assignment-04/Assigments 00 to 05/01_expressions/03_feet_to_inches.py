inch: int = 12 

def foot():
    feet: float = float(input("Enter number of feet: "))
    print(f"There are {feet * inch} inches in {feet} feet")

if __name__ == "__main__":
    foot()