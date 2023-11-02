
products=[
    {"name":"apple","price":120},
    {"name":"mango","price":140},
    {"name":"banana","price":60},
    {"name":"chiku","price":90}
]

affor=list(filter(lambda item : item["price"]<100,products))


for i in affor:
    print(i["name"],i["price"])
