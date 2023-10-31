# Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data
import json

json_response='''
{
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
'''

my_string=json_response
#my_string = my_string.replace("\n", "")
#my_string = my_string.replace(" ", "")
my_string = my_string.replace("False","false")
my_string = my_string.replace("True","true")
print(my_string)
json_dict = json.loads(my_string)
print(json_dict)
print("Booking Id is :",json_dict.get("bookingid"))
print("Check In date is : ",json_dict.get("booking").get('bookingdates').get('checkin'))
print("Check In date is : ",json_dict["booking"]["bookingdates"]["checkin"])
print("Check out date is : ",json_dict.get("booking").get('bookingdates').get('checkout'))
print("Check In date is : ",json_dict["booking"]["bookingdates"]["checkout"])