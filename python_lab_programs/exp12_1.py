# Experiment 12, Form 1: Sum of digits using a while loop
n = int(input("Enter an integer: "))
total = 0
temp = abs(n)

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("The sum of digits of", n, "is:", total)
