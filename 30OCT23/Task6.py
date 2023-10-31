
dict={}

while True:
    res=input("Do you want to enter Y/N : ")
    if res=='Y' or res=="y":
        k=input("enter key : ")
        v=input("enter value : ")
        dict.update({k:v})
    else:
        break

print(dict)

