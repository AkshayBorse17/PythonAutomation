# Method 1 : Find the maximum and minimum elements in a tuple.

my_tuple = (15, 8, 25,36,42,10)

max=my_tuple[0]
for i in my_tuple:
    if max<=i:
        max=i

print("max is : ",max)

max=my_tuple[0]
for i in my_tuple:
    if max>=i:
        max=i

print("min is : ",max)




# Method 2 :  Find the maximum and minimum elements in a tuple.

# my_tuple = (15, 8, 25,36,42,10)

# print(max(my_tuple))

# print(min(my_tuple))