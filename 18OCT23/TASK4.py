
Num=int(input("enter no : "))
# F0,F1=0,1
def call(Num):
    F0,F1=0,1
    if Num<0:
    # print("Enter Positive number")
        Num = int(input("enter Positive number : "))
        call(Num)
    elif Num==0:
        print("Series :", F0)
    else:
        # print("Series :", end="\t")
        for i in range(1, Num):
            print(F0, end=" ")
            Sum = F0+F1
            F0 = F1
            F1 = Sum

        print("\n",F0)

call(Num)