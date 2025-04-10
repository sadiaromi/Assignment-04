def temperature():
    fahrenheit_degree = float(input("Enter temperature in Fahrenheit: "))
    celsius_degree = ((fahrenheit_degree - 32) * 5.0/9.0) 
    print(f"Temperature {fahrenheit_degree}F = {celsius_degree}C")

if __name__ == "__main__":
        temperature()