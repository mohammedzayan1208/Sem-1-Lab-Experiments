# Experiment 23: Main program to import and use the Fibonacci module
from fibonacci_module import fibonacci

n = int(input("Enter the number of terms for Fibonacci series: "))
series = fibonacci(n)

print("Fibonacci series up to", n, "terms:")
print(series)
