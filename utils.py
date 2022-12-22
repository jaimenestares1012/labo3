
from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://user_jaime:XhA7pqTDWKfQy6Nh@micluster.pns9q58.mongodb.net")
db  = client.get_database("catalogos")


def BuscarMongoCatalogos2(valor, coleccion):
    col = db[coleccion]
    try:
        id = col.find({"creador": valor})
        return id
    except NameError:
        print(NameError)


def BuscarMongoGeneric( valor, coleccion, valorBusqueda):
    print("valor", valor)
    print("coleccion", coleccion)
    print("valorBusqueda", valorBusqueda)
    col = db[coleccion]
    try:
        id = col.find_one({valorBusqueda : str(valor) })
        return id
    except NameError:
        print(NameError)

class getCatalogos():
    def __init__(self, colecciones, categorias):
        self.colecciones = colecciones
        self.categorias = categorias

    def logica(self):
        coleccionCompleta = []
        for tienda in self.colecciones:
            busqueda  = BuscarMongoGeneric( tienda ,self.categorias, "idTienda")
            response = {
                "idTienda": busqueda["idTienda"],
                "categorias": busqueda["coleccion"]
            }
            print("<---   response ultils Catalogo  -----> ")
            print("")
            print(response)
            coleccionCompleta.append(response)
        return coleccionCompleta

    def logica2(self):
        coleccionCompleta = []
        for tienda in self.colecciones:
            busqueda = []
            print("<------------- INICIO --------------------->")
            busqueda  = BuscarMongoCatalogos2( tienda , self.categorias)
            array = list(busqueda)
            response = {
                "creador": tienda,
                "data": array
            }
            coleccionCompleta.append(response)
            
        print("buscando el fin")
        return coleccionCompleta


    def busquedaId(self):
        busqueda  = BuscarMongoGeneric(  self.categorias,  self.colecciones , "_id")
        return busqueda



