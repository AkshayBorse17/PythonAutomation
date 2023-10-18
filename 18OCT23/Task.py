user = int(input("Please enter your number:\n"))
n1 = 0
n2 = 1
c = 1

print("Fibonacci Series:", n1, n2, end=" ")

for i in range(2, user):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3

# for i in range(user):
#     c=c*i
#
# print(f"Factorial value{c}")