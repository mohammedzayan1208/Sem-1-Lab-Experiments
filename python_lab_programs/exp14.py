# Experiment 14: Merge two lists with even numbers first and odd numbers next
list1 = []
list2 = []

n1 = int(input("Enter the number of elements in first list: "))
for i in range(n1):
    num = int(input("Enter element: "))
    list1.append(num)

n2 = int(input("Enter the number of elements in second list: "))
for i in range(n2):
    num = int(input("Enter element: "))
    list2.append(num)

merged = list1 + list2
even = []
odd = []

for i in merged:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort()
final = even + odd

print("Merged and sorted list:", final)
