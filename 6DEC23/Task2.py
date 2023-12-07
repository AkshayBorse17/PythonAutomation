import requests as req
import pytest

url = "https://restful-booker.herokuapp.com./booking/"
tokenurl = "https://restful-booker.herokuapp.com/auth"


def test_tokencreate():
    head = {
        "Content-Type": "application/json",
        "Accept": "*/*"
    }
    payload = {
        "username": "admin",
        "password": "password123"
    }
    res = req.post(url=tokenurl, headers=head, json=payload)
    data = res.json()
    print(data)
    global token
    tokendata = data["token"]
    token="token="+tokendata


def test_create():
    head = {}
    payload = {
        "firstname": "pat",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    res = req.post(url=url, headers=head, json=payload)
    print(res.json())
    data = res.json()
    global bookid
    bookid = data["bookingid"]


def test_read():
    res = req.get(url=url + str(bookid))
    print(res.json())


def test_fullupdate():
    head = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Cookie": token
    }
    payload = {
        "firstname": "Raju",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    res = req.put(url=url + str(bookid), headers=head, json=payload)
    print(res.json())

def test_partialupdate():
    head = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Cookie": token
    }
    payload = {
        "firstname": "Raju",
        "lastname": "Herapheri",
    }

    res = req.patch(url=url + str(bookid),headers=head,json=payload)
    print(res.json())

def test_delete():
    head = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Cookie": token
    }
    res=req.delete(url+str(bookid),headers=head)
    print(res.text)
