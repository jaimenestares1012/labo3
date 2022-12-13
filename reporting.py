from pymongo import MongoClient
import json
from datetime import datetime, timedelta

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


class reporteTipo1():
    def __init__(self, nombre, categoria, numeroDias):
        self.nombre = nombre
        self.categoria = categoria
        self.numeroDias = numeroDias
    def teardown_method(self):
        print("aea")

    def logica(self):
        busqueda  = BuscarMongoXNombre(self.categoria, self.nombre)
        array = list(busqueda)
        arregloFiltrado = []
        for a in array:
            i = 0
            dias = int(self.numeroDias)
            selection=[]
            while i <= dias:
                fechaDateTime = datetime.now() - timedelta(i)
                fechaExtraccion = fechaDateTime.strftime("%Y-%m-%d %H:%M:%S") 
                fechaExtraccion2 = fechaExtraccion.split(" ")
                fechaExtraccionclean = fechaExtraccion2[0]
                selection.append(fechaExtraccionclean)
                i = i + 1
            response={}
            filtered = filter(lambda i: i[0] in selection, a.items())
            listPrecios = [dict(list(filtered))]
            response = {
                "nombre" : a["nombre"],
                "url": a["url"],
                "categoria": a["categoria"],
                "tienda": a["tienda"],
                "listPrecios": listPrecios
            }
            arregloFiltrado.append(response)
        return arregloFiltrado 