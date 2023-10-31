ll=[2,3,4,"ABA",5,"cdc","llll","cC","1"]

count=0
for i in ll:
    if len(i)>=2 and i[0]==i[-1]:
        count=count+1

print("Total strings : ",count)