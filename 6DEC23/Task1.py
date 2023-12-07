import pytest
import requests as req

url="https://restful-booker.herokuapp.com./booking"
header={}
# header={
    # "Accept" : "*/*",
    # "Content-Type" : "application/json"
# }
payload={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
res=req.post(url=url,headers=header,json=payload)
data=res.json()

assert data["bookingid"] is not None,"TC1 fail"
assert data["booking"]["firstname"]=="Jim" ,"TC2 fail"
assert data["booking"]["firstname"]=="Jim" ,"TC3 fail"
assert res.status_code==200, "TC4 fail"
assert res.elapsed.microseconds<1000000, "TC5 fail"
