import pickle
import webscrapping as ws
import input_ls as il

import pickle

import pickle

def prediction(url):
    try:
        x = il.features(url, ws.webcontent(url))
        # Check if the shape of x matches the expected shape
        if len(x[0]) != 1139:
            raise ValueError("Feature shape mismatch")
    except Exception as e:
        return "Domain name not registered. Be careful!"
    
    filename = 'finalized_model.sav' 
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(x)
    
    if not result:
        return f'Happy browsing!!!! It is a benign website :{result}'
    else:
        return 'Be careful!!!! It is a malicious website'


#print(prediction('thcvaporizer.com'))
