s1="PPPP"
s2="pppp"
s3="abccDEE"

#id of string
print(id(s1))
print(id(s2))

#lower
s1=s1.lower()
print(s1)

#capitalize
print(s3.capitalize())
print(s3.title())


#upper
s2=s2.upper()
print(s2)

#length
print(len(s1))
print(len(s2))

#swapcase
s3=s3.swapcase()
print(s3)

#title
s4="sdsdsd sdsdsdsdsd sdsdsdDD"
print(s4.title())

#replace
s5="Hello AB"
s5=s5.replace("Hello","Bye")
print("*******",s5)

#index
s6="Hiiii ABIIIhHi"
print(s6.index("Hi"))

#find char
s6="Hiiii ABIIIhHi"
print(s6[8])

#count
print(s6.count("Hi"))


# if s1==s2:
#     print("yes")
# else:
#     print("no")