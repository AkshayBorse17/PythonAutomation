ls=[
    {"bookingid": 2384},
    {"bookingid": 5000},
    {"bookingid": 3000},
    {"bookingid": 2868},
    {"bookingid": 2334},
    {"bookingid": 9090},
    {"bookingid": 7777},
    {"bookingid": 1111},
    {"bookingid": 888},
    {"bookingid": 444},
    {"bookingid": 4999},
    {"bookingid": 399}
]

con=list(filter(lambda item :item["bookingid"]>2000,ls))

for i in con:
    print(i)