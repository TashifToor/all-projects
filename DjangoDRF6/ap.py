import requests
import json

URL="http://127.0.0.1:8000/sapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
get_data()

def create_data():
    data={
        'name':'toorrrrrrrrrrrrrrrrrrrr',
        'roll':23,
        'city':'kashmir',
    }
   
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
create_data()


def update_data():
    data={
        'id':2,
        'name':'faisal',
        
        'city':'dgk',
    }
   
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
update_data() 


def delete_data():
    data={'id':5,}
   
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
delete_data()          
                        
                
        
        