def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Select conversion type (1/2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice")
        return
    
    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    if choice == '1':
        result = (value * 9/5) + 32
        print(f"{value} Celsius is equal to {result} Fahrenheit")
    else:
        result = (value - 32) * 5/9
        print(f"{value} Fahrenheit is equal to {result} Celsius")

def length_converter():
    print("Length Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    
    choice = input("Select conversion type (1/2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice")
        return
    
    try:
        value = float(input("Enter the length value: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    if choice == '1':
        result = value * 3.28084
        print(f"{value} meters is equal to {result} feet")
    else:
        result = value / 3.28084
        print(f"{value} feet is equal to {result} meters")

def weight_converter():
    print("Weight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    
    choice = input("Select conversion type (1/2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice")
        return
    
    try:
        value = float(input("Enter the weight value: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    if choice == '1':
        result = value * 2.20462
        print(f"{value} kilograms is equal to {result} pounds")
    else:
        result = value / 2.20462
        print(f"{value} pounds is equal to {result} kilograms")

# Main program
while True:
    print("\nUnit Converter Menu:")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    print("4. Exit")
    
    choice = input("Select the type of converter (1/2/3/4): ")
    
    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    elif choice == '4':
        print("Exiting Unit Converter. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
