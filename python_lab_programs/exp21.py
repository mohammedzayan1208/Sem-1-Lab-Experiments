# Experiment 21: Recursive multiplication using repeated addition
def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

if a < 0 or b < 0:
    print("Please enter positive integers only.")
else:
    result = multiply(a, b)
    print("The product of", a, "and", b, "is:", result)
