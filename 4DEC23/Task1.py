import requests as req

resp=req.get("https://restful-booker.herokuapp.com./booking/704")
# print(resp.headers)
# print(resp.status_code)
data=resp.json()

assert "firstname" in data,"not present"
assert "lastname" in data,"not present"

assert resp.status_code==200,"not present"
assert data["firstname"]=="Jim","not present"
assert data["lastname"]=="Brown","not present"


