# Experiment 11, Form 1: Fibonacci series using conditional statements and a loop
count = int(input("Enter the number of terms: "))

if count <= 0:
    print("Enter a positive number of terms.")
elif count == 1:
    print("0")
elif count == 2:
    print("0")
    print("1")
else:
    prev1 = 0
    prev2 = 1
    print(prev1)
    print(prev2)

    for i in range(count - 2):
        next_term = prev1 + prev2
        print(next_term)
        prev1 = prev2
        prev2 = next_term
