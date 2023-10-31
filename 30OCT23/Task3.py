# Method 1 : Remove duplicate elements from a list.

my_list = [1,8, 2, 2, 3, 1,4,8, 4, 5]

new_list=[]

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(f'Original string : {my_list}')
print(f'New unique list : {new_list}')



# Method 2 : Remove duplicate elements from a list.

# my_list = [1,8, 2, 2, 3, 1,4,8, 4, 5]

# new_list = list(set(my_list))

# print(f'Original string : {my_list}')
# print(f'New unique list : {new_list}')
