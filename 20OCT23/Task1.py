
# Palindrome Checker: Method1
name=input("Enter your name : ")

name2=""
for i in name:
    name2=i+name2

print(f'Reverse is : {name2}')

if name==name2:
    print("***Its palindrome")
else:
    print("***Its not palindrome")




# Palindrome Checker: Using slicing Method2

# name=input("Enter your name : ")
# if name==name[::-1]:
#     print("***Its palindrome")
# else:
#     print("***Its not palindrome")