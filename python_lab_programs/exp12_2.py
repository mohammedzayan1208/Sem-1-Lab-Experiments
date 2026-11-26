# Experiment 12, Form 2: Sum of digits using a for loop
n = input("Enter an integer: ")
total = 0

for digit in n:
    if digit.isdigit():
        total += int(digit)

print("The sum of digits of", n, "is:", total)
