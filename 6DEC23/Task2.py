import requests as req
import pytest

url = "https://restful-booker.herokuapp.com./booking/"
tokenurl = "https://restful-booker.herokuapp.com/auth"

@pytest.mark.positive
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
    assert res.status_code == 200, "TC1 Failed"
    assert "token" in data, "TC2 failed"
    assert res.elapsed.microseconds < 1000000, "TC3 Failed"

@pytest.mark.positive
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
    assert res.status_code == 200, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data["bookingid"] is not None, "TC3 failed"
    assert data["booking"]["firstname"] is not None, "TC4 failed"
    assert data["booking"]["firstname"]=="pat", "TC5 failed"


@pytest.mark.positive
def test_read():
    res = req.get(url=url + str(bookid))
    print(res.json())
    data=res.json()
    assert res.status_code == 200, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data["firstname"] is not None, "TC3 failed"
    assert data["lastname"] is not None, "TC4 failed"
    assert data["firstname"] == "pat", "TC5 failed"


@pytest.mark.positive
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
    data=res.json()
    print(res.json())
    assert res.status_code == 200, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data["firstname"] is not None, "TC3 failed"
    assert data["lastname"] is not None, "TC4 failed"
    assert data["firstname"] == "Raju", "TC5 failed"


@pytest.mark.negative
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
    data=res.json()
    assert res.status_code == 200, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data["firstname"] is not None, "TC3 failed"
    assert data["lastname"] is not None, "TC5 failed"
    assert data["firstname"] == "Raju", "TC5 failed"

@pytest.mark.positive
def test_delete():
    head = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Cookie": token
    }
    res=req.delete(url+str(bookid),headers=head)
    print(res.text)
    data=res.text
    assert res.status_code == 201, "TC1 failed"
    assert res.elapsed.microseconds < 1000000, "TC2 failed"
    assert data == "Created", "TC3 failed"
