# Experiment 15: Concatenate two strings and display a substring
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + str2
print("Concatenated string:", result)

start = int(input("Enter starting position: "))
end = int(input("Enter ending position: "))

substring = result[start:end]
print("Substring:", substring)
