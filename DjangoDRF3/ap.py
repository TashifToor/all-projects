import requests
import json

URL="http://127.0.0.1:8000/stucreate/"

data={
    'name':'tashif',
    'roll':21,
    'city':'lahore',
}

json_data=json.dumps(data)#main dumps method
r=requests.post(url=URL,data=json_data)

data=r.json()
print(data)