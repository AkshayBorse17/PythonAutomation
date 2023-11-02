
ls=["apple","banana","chiku","mango","organge"]
ls2=[]

def len_check(x):
    return len(x)>5

length=list(filter(len_check,ls))

print(length)