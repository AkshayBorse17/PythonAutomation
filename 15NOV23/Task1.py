from collections import Counter
ll=[2,3,4,3,3,2,0,2,3]

con=Counter()
for i in ll:
    con[i]+=1

print(type(con))