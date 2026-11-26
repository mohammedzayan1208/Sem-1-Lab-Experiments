# Experiment 20: Recursive addition
def add(a, b):
    if b == 0:
        return a
    else:
        return add(a + 1, b - 1)

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

if a < 0 or b < 0:
    print("Please enter positive integers only.")
else:
    result = add(a, b)
    print("The sum of", a, "and", b, "is:", result)
