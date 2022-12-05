from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://user_jaime:XhA7pqTDWKfQy6Nh@micluster.pns9q58.mongodb.net")
db  = client.get_database("tesis-metro")

def BuscarMongoXNombre(coleccion ,valor):
    col = db[coleccion]
    try:
        col.create_index([('nombre', 'text')])
        id = col.find({"$text": {"$search": valor}})
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
        array = list(busqueda)
        return array 