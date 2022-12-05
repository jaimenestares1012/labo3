from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://user_jaime:XhA7pqTDWKfQy6Nh@micluster.pns9q58.mongodb.net")
db  = client.get_database("tesis-metro")
# cliente=MongoClient('localhost')
# db=cliente['tesis-won']

def BuscarMongoXNombre(coleccion ,valor):
    col = db["lacteos"]
    try:
        id = col.find_one({"_id": "572685"})
        print("sñssssssssssssssss", id)
        return id
    except NameError:
        print("ERROR")
        print(NameError)


class reporteTipo1():
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def teardown_method(self):
        print("aea")

    def logica(self):
        busqueda  = BuscarMongoXNombre(self.categoria, self.nombre)
        # array = list(busqueda)
        # return array
        return {"goo": "sssssssssssssssssssssssssssssss"}   