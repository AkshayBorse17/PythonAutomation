# Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

dict={

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}

print(dict)

print("Booking id : ",dict.get("bookingid"))
print("Checkin : ",dict.get("booking").get("bookingdates").get("checkin"))
print("Checkout : ",dict.get("booking").get("bookingdates").get("checkout"))
