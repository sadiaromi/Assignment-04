import random

num_sides: int = 6

def dice():
    die1: int = random.randint(1,6)
    die2: int = random.randint(1,6)
    total: int = int(die1 + die2)
    print("Dice have", num_sides, "sides each")
    print("First die: " + str(die1))
    print("Second die: " + str(die2))
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    dice()