from pymongo import MongoClient
from datetime import datetime, timedelta
import matplotlib.pyplot as pl
import json
import base64

client = MongoClient("mongodb+srv://user_jaime:XhA7pqTDWKfQy6Nh@micluster.pns9q58.mongodb.net")
db  = client.get_database("catalogos")



def get_as_base64(url):
    image = open(url, 'rb')  # open binary file in read mode
    image_read = image.read()
    # print("image_read", image_read)
    image_64_encode = base64.b64encode(image_read)

    # ### de bytes a string
    to_string = image_64_encode.decode("utf-8")
    return to_string

def BuscarMongo(coleccion):
    col = db[coleccion]
    try:
        id = col.find()
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
        print("logica")
        res = BuscarMongo("variacionDolar")
        arrayDolar = []
        arrayFechasDolar = []
        for b in list(res):
            print("<---->", b)
            mien2 = b["Fecha"].replace(".2022", "")
            arrayDolar.append(round(float(b["Último"].replace("," , ".")), 2))
            arrayFechasDolar.append(mien2.replace(".", "-"))

        for a in self.json["data"]:
            mien = a["fecha"].replace("2022-", "")
            arrayGlobal.append(a["montoTotal"])
            arrayFechas.append(mien)
        
        print("arrayFechasDolar", arrayFechasDolar)
        print("arrayDolar", arrayDolar)
        # x =[1000,1004,999]
        # y =["2022-12-23", "2022-12-22", "2022-12-21"]
        
        # # y = ()
        # print("logica", x)
        pl.plot(arrayFechas, arrayGlobal,  'b--o')
        pl.savefig("data")
        plt_1 = pl.figure(figsize=(13,4))
        pl.plot(arrayFechasDolar, arrayDolar ,  'b--o')
        pl.savefig("dataDolar")


        try:
            rbase64 = get_as_base64('data.png')
            dbase64 = get_as_base64('dataDolar.png')
            data = {
                "producto":rbase64,
                "dolar":dbase64
            }
            return data
        except NameError:
            print("errorr")
            print(NameError)
            return {}
