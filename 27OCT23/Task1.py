
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

print(f'The largest no is : {max(ll)}')

