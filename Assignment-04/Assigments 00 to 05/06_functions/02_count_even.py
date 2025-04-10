def count_even():
    numbers = []  

    while True:
        user_input = input("Enter an number: ")
        
        if user_input == "":  
            break
        
        try:
            num = int(user_input)  
            numbers.append(num) 
        except ValueError:  
            print("❌ Invalid input! Please enter a valid integer.")

    
    even_count = sum(1 for num in numbers if num % 2 == 0)
    print(f"Total even numbers: {even_count}")

count_even()
