# Experiment 2, Form 1: Reverse a three-digit number using mathematics
num = int(input("Enter a three-digit number: "))
rev = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
print("Reversed number:", rev)
