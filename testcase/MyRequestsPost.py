import requests
import json
url="http://pycmstsl.lexue.com/basic/school/saveSchool"
payload = {"bigAreaId": "103","provinceId": "210000","cityId": "210100","bigAreaName": "东北","provinceName": "辽宁省","cityName": "沈阳市","schoolName": "pyth1on北学校","branchGrade": "1"}
headers = {"appKey":"201820011141153","isAdmin":"2","Content-Type":"application/json","token":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNzAxIiwic3ViIjoi5a2f56Wl5bGxIiwiaWF0IjoxNTc2NzQwMzYzLCJleHAiOjE1NzY4MjY3NjN9.rBqlpFQsC1CAA30cGT0iAik0RC-t8uIB-pgHKn3PSLU","userId":"2701","signature":"79E48482F30ED5CA96DCBB4DFA43D1576DBC2B74"}
print(type(json.dumps(payload)))
print(type(payload))
r = requests.post(url, headers=headers,data=json.dumps(payload))
print(r.text)