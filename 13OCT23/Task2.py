# Area of circle :
rad=float(input("Enter radius of circle : "))
pi=22/7
area=pi*(rad**2)
print(area)


# No Greate than or less than
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
if num1>num2:
    print(f'num 1 is greater')
elif num2>num1:
    print(f'num 2 is greater')
else:
    print(f'Both are euals')


# Maximum of three numbers using ternary operator
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
num3=int(input("Enter num3 : "))
max=num1 if num1>num2 and num1>num3 else num2 if num2>num1 and num2>num3 else num3

print(f'Maximum no is {max}')


# Script to calculate square and cube of number :
num=float(input("Enter Number : "))
square=num**2
cube=num**3
print(f'Square is: {square} and cube is: {cube}')