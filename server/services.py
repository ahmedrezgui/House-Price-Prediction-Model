import json
import pickle
import numpy as np


__states=None
__cities=None
__data_columns=None
__model=None

def get_estimated_price(state,city,latitude,longitude,bedroom,bathroom,area,lotarea):
    try:
        state_index=__data_columns.index(state.lower())
    except:
        state_index=-1

    try:       
        city_index=__data_columns.index(city.lower())
    except:
        city_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=latitude
    x[1]=longitude
    x[2]=bedroom
    x[3]=bathroom
    x[4]=area
    x[5]=lotarea
    if state_index>=0:
        x[state_index]=1
    if city_index>=0:
        x[city_index]=1    

    
    return round( __model.predict([x])[0],2)

def get_states():
    return __states

def get_cities():
    return __cities

def load_artifacts():
    print('Loading Artifacts...')
    global __data_columns
    global __states
    global __cities
    global __model

    with open ("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __states=__data_columns[6:54]
        __cities=__data_columns[55:]

    with open('./artifacts/house_price_prediction_model.pickle','rb') as f:
        __model=pickle.load(f)    


if __name__ == '__main__':
    load_artifacts()
    print(get_states())  
    print(get_cities())
    print(get_estimated_price('ca','los angeles',34.0522,-118.2437,3,2,1500,5000)  )
    print(get_estimated_price('ca','los angeles',34.0522,-118.2437,4,4,2000,5000)  )