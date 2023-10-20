# Finonacci Series-using function

Num=int(input("Enter no : "))
def call(Num):
    F0,F1=0,1


    if Num<0:
        Num = int(input("Enter Positive number : "))
        call(Num)

    elif Num==0:
        print("Fibonacci Series :", F0)
        print("Fibonacci Sum : ", F0)

    else:
        print("Fibonacci Series :", end="\t")
        for i in range(0, Num+1):
            print(F0, end=" ")
            if i==Num:

                break
            Sum = F0 + F1
            F0 = F1
            F1 = Sum
        # print(F0)
        print("\nFibonacci Sum : ",F0)
call(Num)



# Finonacci Series-Without using function

# Num = int(input("Enter number : "))
#
# F0, F1 = 0, 1
#
# if Num < 0:
#     print("Enter Positive number..")
#
# elif Num == 0:
#     print("Fibonacci Series :", F0)
#     print("Fibonacci Sum : ", F0)
#
# else:
#     print("Fibonacci Series :", end="\t")
#     for i in range(0, Num + 1):
#         print(F0, end=" ")
#         if i == Num:
#             break
#         Sum = F0 + F1
#         F0 = F1
#         F1 = Sum
#
#     print("\nFibonacci Sum : ", F0)