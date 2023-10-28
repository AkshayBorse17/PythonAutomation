
ll=[]
while True:
    num=int(input("Enter number : "))
    res=input("Do you want to add again Y/N : ")

    if res=="Y" or res=="y":
        ll.append(num)
    else:
        ll.append(num)
        break

print(ll)

mul=1
for i in ll:
    mul=mul*i

print(f'Multiplication of numbers : {mul}')


