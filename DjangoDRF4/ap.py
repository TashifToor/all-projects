import requests
import json

URL="http://127.0.0.1:8000/studata/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
    
get_data()  

def create_data():
    data={
        'name':'ali',
        'roll':132,
        'city':'krachi',
    }
    
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
 
create_data() 


def update_data():
    data={
        'id':3,
        'name':'rajaaaa',
        'city':"kashmir",
        
    }        
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
    
update_data() 


def delete_data():
    data={'id':12}        
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
    
delete_data()    
    
    