# Experiment 13, Form 2: Prime numbers less than N using nested loops
N = int(input("Enter a positive integer N: "))
print("Prime numbers less than", N, "are:")

for num in range(2, N):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
