try:
    a=4
    b=int(input("enter num : "))
    print(a/b)

except Exception as err:
    print(err)
else:
    print("no exception")
finally:
    print("hello")