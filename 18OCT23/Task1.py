# Factorial Series

num=int(input("Enter number : "))

if num>=0:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
else:
    print("Please enter positive number")


