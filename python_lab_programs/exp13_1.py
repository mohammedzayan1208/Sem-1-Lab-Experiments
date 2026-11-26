# Experiment 13, Form 1: Prime numbers less than N using a function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input("Enter a positive integer N: "))
print("Prime numbers less than", N, "are:")

for number in range(2, N):
    if is_prime(number):
        print(number, end=" ")
print()
