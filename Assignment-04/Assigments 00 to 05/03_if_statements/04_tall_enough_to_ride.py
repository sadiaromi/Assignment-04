min_height: int = 50

def main():
  user: int = int(input("How tall are you? "))
  if user >= min_height:
    print("You're tall enough to ride!")
  else:
    print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
   main()