from pymongo import MongoClient
from datetime import datetime, timedelta
import json

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


def BuscarMongo(coleccion ,valor):
    col = db[coleccion]
    try:
        id = col.find_one({"nombre": valor})
        return id
    except NameError:
        print("ERROR")
        print(NameError)
    print("buscat")

class poderWon():
    def __init__(self, numeroDias, productos):
        self.numeroDias = numeroDias
        self.productos = productos

    def teardown_method(self):
        print("aea")

    def logica(self):
        fechasDisponibles = []
        i = 1
        dias = int(self.numeroDias)
        while i <= dias:
            fechaDateTime = datetime.now() - timedelta(i)
            fechaExtraccion = fechaDateTime.strftime("%Y-%m-%d %H:%M:%S") 
            fechaExtraccion2 = fechaExtraccion.split(" ")
            fechaExtraccionclean = fechaExtraccion2[0]
            fechasDisponibles.append(fechaExtraccionclean)
            i = i + 1

        data = []
        for a in self.productos:
            busquedaProductos = BuscarMongo(a["typeCategory"], a["prod"])
            busquedaProductos["cantidad"] = a["cantidad"]
            data.append(busquedaProductos)
        dataxdiaGlobal =[]
        # for b in data:
        #     print("este es mi b", b)
        #     for a in fechasDisponibles:
        #         dataxdia =[]
        #         print("<-------------- FECHAAA ------------------->", a)
        #         try:
        #             datos = {
        #                 "producto": b["nombre"],
        #                 "precio": b[a]
        #             }
        #             dataxdia.append(datos)
        #             datos = {}
        #             print("dataxdia", dataxdia)
        #         except:
        #             datos = {}
                
        #         dataParcial = {
        #             "fecha": a,
        #             "productosXFecha":dataxdia
        #         }
        #         print("data parcial", dataParcial)
        #         dataxdiaGlobal.append(dataParcial)
        #         # print("dataxdiaGlobal", dataxdiaGlobal)
        #         dataParcial = {}
        #         print("<-------------- FIN  ------------------->")
        
        print("data", data)
        for a in fechasDisponibles:
            print(" FECHAAA ---->", a)
            dataxdia =[]
            contador = len(data)
            it = 1
            suma = 0
            for b in data:
                try:
                    price = b[a]
                    price = price.split("S/")
                    precioLimpio = price[1].replace(" ", "")
                    precioLimpio = float(precioLimpio)
                    sumaParcial = int(b["cantidad"]) * float(precioLimpio)
                    datos = {
                        "producto": b["nombre"],
                        "precio": precioLimpio,
                        "cantidad": b["cantidad"],
                        "sumaParcial": sumaParcial
                    }
                    suma = suma + sumaParcial
                    dataxdia.append(datos)
                    datos = {}
                except:
                    datos = {}
                
                dataParcial = {
                    "fecha": a,
                    "montoTotal": suma,
                    "numeroProductos": len(dataxdia),
                    "productosXFecha":dataxdia
                }
                
                if len(dataParcial["productosXFecha"])> 0 and contador == it:
                    # print("dataParcial", dataParcial)
                    dataxdiaGlobal.append(dataParcial)
                dataParcial = {}
                it = it + 1         
        return dataxdiaGlobal 