from pymongo import MongoClient
from datetime import datetime, timedelta
import matplotlib.pyplot as pl
import json
import base64
from os import remove

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
        id = col.find().limit(30)
        return id
    except NameError:
        print("ERROR")
        print(NameError)
    print("buscat")

class resumenRep():
    def __init__(self, json):
        self.json = json

    


    def logica(self):
        pl.figure(figsize=(14,4))
        print("logica")
        res = BuscarMongo("variacionDolar")
        arrayDolar = []
        arrayFechasDolar = []
        for b in list(res):
            mien2 = b["Fecha"].replace(".2022", "")
            arrayDolar.append(round(float(b["Último"].replace("," , ".")), 2))
            arrayFechasDolar.append(mien2.replace(".", "-"))
        print("-")
        print("-")
        print("arrayDolar", arrayDolar, len(arrayDolar))
        print("arrayFechasDolar", arrayFechasDolar, len(arrayFechasDolar))

        pl.plot(arrayFechasDolar, arrayDolar ,  'b--o')
        pl.title("Variación del dólar")
        pl.xlabel("Precio (S/)")
        pl.ylabel("Día-Mes")
        pl.savefig("dataDolar")

        print("FIN IMAGEN ---- DOLAR")
        arrayGlobal = []
        arrayFechas = []
        for a in self.json["data"]:
            mien = a["fecha"].replace("2022-", "")
            arrayGlobal.append(a["montoTotal"])
            arrayFechas.append(mien)
        pl.figure(figsize=(14,4))
        pl.plot(arrayFechas, arrayGlobal,  'b--o')
        pl.title("Variación de la canasta")
        pl.xlabel("Costo total (S/)")
        pl.ylabel("Día-Mes")
        pl.savefig("data")
        print("-")
        print("-")
        print("arrayGlobal", arrayGlobal, len(arrayGlobal))
        print("arrayFechas", arrayFechas, len(arrayFechas))
        
       


        try:
            rbase64 = get_as_base64('data.png')
            dbase64 = get_as_base64('dataDolar.png')
            remove("data.png")
            remove("dataDolar.png")
            arrayGlobal = []
            arrayFechas = []
            arrayDolar = []
            arrayFechasDolar = []
            data = {
                "producto":rbase64,
                "dolar":dbase64
            }
            return data
        except NameError:
            print("errorr")
            print(NameError)
            return {}
