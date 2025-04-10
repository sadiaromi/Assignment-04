import random

DONE_LIKELIHOOD = 0.3 

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for num in range(1, 11):
        if done():
            return  
        print(num)  

def main():
    chaotic_counting()
    print("I'm done.")  

if __name__ == "__main__":
    main()