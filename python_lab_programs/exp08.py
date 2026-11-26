# Experiment 8: Factorial of a number using a loop
n = int(input("Enter a number: "))
fact = 1

for f in range(1, n + 1):
    fact *= f

print("The factorial of", n, "is", fact)
