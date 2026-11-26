# Experiment 11, Form 2: Fibonacci series using a for loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
