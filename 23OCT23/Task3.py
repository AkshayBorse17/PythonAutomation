
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))

def calculate(num1,num2):
    return num1^num2

cal=calculate(num1,num2)
print(f'{num1}^{num2} is : {cal}')