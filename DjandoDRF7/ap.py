import requests
import json

URL="http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id',id}
    headers={'content-type':'application/json'}    
    json_data=json.dumps(data)
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)   

get_data()

def create_data():
    data={
        'name':'tashif',
        'roll':15,
        'city':'krachi',
    }
    headers= {'content-type':'application/json'}    
    
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
 
create_data() 

             