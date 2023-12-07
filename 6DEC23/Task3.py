import pytest
import requests as req

url = "https://restful-booker.herokuapp.com./booking/"
tokenurl = "https://restful-booker.herokuapp.com/auth"

@pytest.mark.positive
def test_tokenCreate():
    header = {}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    res = req.post(url=tokenurl, headers=header, json=payload)
    data = res.json()
    print(data)
    token = data["token"]
    assert res.status_code==200, "TC1 Failed"
    assert "token" in data, "TC2 failed"
    assert res.elapsed.microseconds<1000000 , "TC3 Failed"
    return token

@pytest.mark.positive
def test_create():
    header = {}
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
    res = req.post(url=url, headers=header, json=payload)
    data = res.json()
    print(data)
    bookid = data["bookingid"]
    assert res.status_code==200, "TC1 failed"
    assert res.elapsed.microseconds<1000000, "TC2 failed"
    assert data["bookingid"] is not None, "TC3 failed"
    assert data["booking"]["firstname"] is not None, "TC4 failed"
    assert data["booking"]["firstname"]=="pat", "TC5 failed"
    return bookid

@pytest.mark.positive
def test_read():
    header = {}
    payload = {}

    res = req.get(url=url + str(test_create()))
    data = res.json()
    print(data)
    assert res.status_code == 200, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data["firstname"] is not None, "TC3 failed"
    assert data["lastname"] is not None, "TC4 failed"
    assert data["firstname"]=="pat", "TC5 failed"

@pytest.mark.positive
def test_fullUpdate():
    token="token="+test_tokenCreate()
    header = {
        "Cookie" : token
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
    res = req.put(url=url + str(test_create()), headers=header, json=payload)
    data = res.json()
    print(data)
    assert res.status_code == 200, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data["firstname"] is not None, "TC3 failed"
    assert data["lastname"] is not None, "TC4 failed"
    assert data["firstname"]=="Raju", "TC5 failed"


@pytest.mark.negative
def test_partialUpdate():
    token="token="+test_tokenCreate()
    header={
        "Cookie" : token
    }
    payload={
        "firstname": "Raju",
        "lastname": "Herapheri",
        "totalprice":18181818
    }
    res=req.patch(url=url+str(test_create()),headers=header,json=payload)
    data=res.json()
    print(data)
    assert res.status_code == 200, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data["firstname"] is not None, "TC3 failed"
    assert data["lastname"] is not None, "TC5 failed"
    assert data["firstname"]=="Raju", "TC5 failed"


@pytest.mark.positive
def test_delete():
    token="token="+test_tokenCreate()
    header={
        "Cookie" : token
    }
    payload={}
    res=req.delete(url=url+str(test_create()),headers=header)
    data=res.text
    print(data)
    assert res.status_code == 201, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data=="Created", "TC3 failed"