import requests
import json

URL="http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)    
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
    
    
get_data(1)
get_data(2)
get_data(3)




def post_data():
    data={
        'name':'sajal',
        'roll':12,
        'city':'multan',
    }
    
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
    
post_data()    




def update_data():
    data={
        'id':1,
        'name':'malik',
        'city':'D.G.K',
    }
    
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
    
update_data() 



def delete_data():
    data={'id':3}
    
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
    
delete_data()    
   





        

