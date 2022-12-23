from pymongo import MongoClient
from datetime import datetime, timedelta
import matplotlib.pyplot as pl
import json
import base64

client = MongoClient("mongodb+srv://user_jaime:XhA7pqTDWKfQy6Nh@micluster.pns9q58.mongodb.net")
db  = client.get_database("tesis-won")

def BuscarMongoXNombre(coleccion ,valor):
    col = db[coleccion]
    try:
        col.create_index([('nombre', 'text')])
        id = col.find({"$text": {"$search": valor}})
        return id
    except NameError:
        print("ERROR")
        print(NameError)


def get_as_base64(url):
    image = open(url, 'rb')  # open binary file in read mode
    image_read = image.read()
    # print("image_read", image_read)
    image_64_encode = base64.b64encode(image_read)

    # ### de bytes a string
    to_string = image_64_encode.decode("utf-8")
    print("to_string", to_string)
    return to_string

def BuscarMongo(coleccion ,valor):
    col = db[coleccion]
    try:
        id = col.find_one({"nombre": valor})
        return id
    except NameError:
        print("ERROR")
        print(NameError)
    print("buscat")

class resumenRep():
    def __init__(self, json):
        self.json = json

    


    def logica(self):
        arrayGlobal = []
        arrayFechas = []
        for a in self.json["data"]:
            print("<---->")
            mien = a["fecha"].replace("2022-", "")
            arrayGlobal.append(a["montoTotal"])
            arrayFechas.append(mien)
        
        print("arrayGlobal", arrayGlobal)
        # x =[1000,1004,999]
        # y =["2022-12-23", "2022-12-22", "2022-12-21"]
        
        # # y = ()
        # print("logica", x)
        pl.plot(arrayFechas, arrayGlobal,  'b--o')
        pl.savefig("data")
        try:
            rbase64 = get_as_base64('data.png')
            return rbase64
        except NameError:
            print("errorr")
            print(NameError)
            return {}
