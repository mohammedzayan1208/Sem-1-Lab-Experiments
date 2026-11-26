# Experiment 17: Check whether three sides form a right triangle
def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        return True
    else:
        return False

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if is_right_triangle(a, b, c):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
