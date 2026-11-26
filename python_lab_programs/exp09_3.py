# Experiment 9, Form 3: Celsius/Fahrenheit conversion using C/F choice
temp = float(input("Enter temperature: "))
choice = input("Convert to (C/F): ")

if choice == 'F' or choice == 'f':
    result = (temp * 9 / 5) + 32
    print("Temperature in Fahrenheit:", result)
elif choice == 'C' or choice == 'c':
    result = (temp - 32) * 5 / 9
    print("Temperature in Celsius:", result)
else:
    print("Invalid choice!")
