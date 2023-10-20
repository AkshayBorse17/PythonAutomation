 # Sum of Digits: Method1

num=input("Enter number : ")

def sumOfDigits(num):
    sum = 0
    if int(num)<0:
        num=input("Please enter positive number : ")
        sumOfDigits(num)
    else:
        for i in num:
            sum=sum+int(i)

        print(f'Sum of digits is : {sum}')
sumOfDigits(num)



#   Sum of Digits: Method2

# num=int(input("Enter number : "))

# def sumOfDigits(num):
#     sum = 0
#     if num<0:
#         num=int(input("Please enter positive number : "))
#         sumOfDigits(num)
#     else:
#         while num>0:
#             rem=int(num%10)
#             sum=sum+rem
#             num=num/10
#             # return sum
#         print(f'Sum of digits is : {sum}')
#
# sumOfDigits(num)
#
# # print(sumOfDigits(num))