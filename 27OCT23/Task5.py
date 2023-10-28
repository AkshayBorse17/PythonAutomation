ll=[2,3,4,"ABA",5,"cdc","llll","cC","1"]

str=""
count=0
for i in ll:
    if type(i)==type(str) and len(i)>=2 and i[0]==i[-1]:
        count=count+1
        # print("yes")
    # else:
        # print("not")

print("Total strings : ",count)