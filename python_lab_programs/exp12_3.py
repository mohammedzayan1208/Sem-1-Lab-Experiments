# Experiment 12, Form 3: Sum of digits using if-else
n = int(input("Enter an integer: "))

if n >= 0:
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    print("The sum of digits of", n, "is:", total)
else:
    print("Please enter a positive integer.")
