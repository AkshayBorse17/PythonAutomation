import requests as req
import pytest
res=req.get("https://restful-booker.herokuapp.com./booking/1617")
data=res.json()

def test_TC1():
    assert 3==3

def test_TC2():
    assert data["firstname"]=="Jim" , "TC1 fail"

def test_TC3():
    assert res.status_code==200,"TC2 fail"

def test_TC4():
    assert data["lastname"] == "Brown", "TC3 fail"





