
Num=int(input("enter no : "))

F0,F1=0,1

if Num<0:
    # print("Enter Positive number")
    Num = int(input("enter Positive number : "))
elif Num==0:
    print("Series :", F0)
elif Num>0:
    # print("Series :", end="\t")
    for i in range(0, Num):
            print(F0, end=" ")
            Sum = F0+F1
            # print(Sum, end=" ")
            F0 = F1
            F1 = Sum
            # print(F0, end=" ")

    print("\n",F0)