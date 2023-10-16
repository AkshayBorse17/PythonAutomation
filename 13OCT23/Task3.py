ss=set()

while True:
    res = input("Do you want to enter data YES/NO : ")
    if res=="YES" or res=="yes" or res=="Yes" or res=="y" or res=="Y":
        data=int(input("Enter data : "))
        # data = input("Enter data : ")
        ss.add(data)
    else:
        break


find=int(input("Search the number : "))
if find in ss:
    print("Its present...")
else:
    newadd=input("Not Present..Do you want to add YES/No : ")
    if newadd == "YES" or newadd == "yes" or newadd == "Yes" or newadd == "y" or newadd == "Y":
        # newnum=input("Enter Number : ")
        ss.add(find)
    # else:
    #     print("Thanks you!!!!")


print(ss)