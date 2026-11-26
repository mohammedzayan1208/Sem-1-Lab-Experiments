# Experiment 9, Form 2: Celsius/Fahrenheit conversion using if-elif
temp = float(input("Enter the temperature value: "))

print("Choose conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    fahrenheit = (temp * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit, "°F")
elif choice == 2:
    celsius = (temp - 32) * 5 / 9
    print("Temperature in Celsius:", celsius, "°C")
else:
    print("Invalid choice! Please enter 1 or 2.")
