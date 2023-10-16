# Write a program that classifies a triangle based on its side lengths.

# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

# Use an if-else statement to classify the triangle.

side1=float(input("Enter side1 : "))
side2=float(input("Enter side2 : "))
side3=float(input("Enter side3 : "))

if side1==side2==side3:
    print(" triangle is equilateral")
elif side1==side2 or side2==side3 or side1==side3:
    print(" triangle is isosceles")
else:
    print(" triangle is scalene")


