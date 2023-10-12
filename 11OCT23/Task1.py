
ss=set()

while True:
    res = input("Do you want to enter data YES/NO : ")
    if res=="YES" or res=="yes" or res=="Yes" or res=="y" or res=="Y":
        # data=int(input("Enter data :"))
        data = input("Enter data : ")
        ss.add(data)
    else:
        break

print(ss)