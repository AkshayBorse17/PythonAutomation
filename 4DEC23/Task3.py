def test_TC1():
    assert 5==5


def test_TC2():
    assert 3 == 3


def test_TC3():
    import requests as req

    resp = req.get("https://restful-booker.herokuapp.com./booking/2088")
    # print(resp.headers)
    # print(resp.status_code)
    data = resp.json()

    assert "firstname" in data, "not present"
    assert "lastname" in data, "not present"

    assert resp.status_code == 200, "not present"
    assert data["firstname"] == "Jim", "not present"
    assert data["lastname"] == "Brown", "not present"
