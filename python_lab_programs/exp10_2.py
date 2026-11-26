# Experiment 10, Form 2: Star pattern using a function
def printPattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

n = int(input("Enter the number of lines: "))
printPattern(n)
