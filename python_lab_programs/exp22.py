# Experiment 22: Recursive GCD using Euclid's algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

if a <= 0 or b <= 0:
    print("Please enter positive integers only.")
else:
    result = gcd(a, b)
    print("The GCD of", a, "and", b, "is:", result)
