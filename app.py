from flask import Flask, request

from flask_cors import CORS
from reporting import reporteTipo1
from reportingtottus import reporteTipo2
from reportingMetro import reporteTipo3

from adquisitivoWon import poderWon

from resumenGraficos import resumenRep
from utils import getCatalogos, usuarios

app = Flask(__name__)
CORS(app)

@app.route('/', methods=[ 'GET'])
def index():
    return {"message": "dededede"}

@app.route('/test', methods=[ 'POST'])
def index2():
    json = request.get_json()
    producto = json["nombreProducto"]
    categoria = json["categoria"]
    return {"producto": producto,
            "categoria": categoria}



@app.route('/get/data/<int:tipo>', methods=[ 'POST'])
def inicio(tipo):
    if tipo == 1:

        print("es tipo 1", tipo)
        json = request.get_json()
        producto = json["nombreProducto"]
        categoria = json["categoria"]
        
        try:
            numeroDias = json["numeroDias"]
        except:
            numeroDias = 10
        
        try:
            numeroProductos = json["numeroProductos"]
        except:
            numeroProductos = 5
        inicio = reporteTipo1( producto, categoria, numeroDias, numeroProductos) 
        datos = inicio.logica()
        data={
            "codRes": "00",
            "detalle": "éxito",
            "data": datos
        }
        return data
    elif tipo == 2:
        print("es tipo 2", tipo)
        json = request.get_json()
        producto = json["nombreProducto"]
        categoria = json["categoria"]
        inicio = reporteTipo2( producto, categoria) 
        datos = inicio.logica()
        print("datos", datos)
        data={
            "codRes": "00",
            "detalle": "éxito",
            "data": datos
        }
        return data
    elif tipo == 3:
        print("es tipo 3", tipo)
        json = request.get_json()
        producto = json["nombreProducto"]
        categoria = json["categoria"]
        inicio = reporteTipo3( producto, categoria) 
        datos = inicio.logica()
        print("datos", datos)
        data={
            "codRes": "00",
            "detalle": "éxito",
            "data": datos
        }
        return data
    else:
        return "tipo incorrecto"

@app.route('/get/poder/<int:tipo>', methods=[ 'POST'])
def poderAdquisitivo(tipo):
    if tipo == 1:
        json = request.get_json()
        creador = json["creador"]
        title = json["title"]
        tienda = json["tienda"]
        productos= json["productosList"]
        try:
            numeroDias = json["numeroDias"]
        except:
            numeroDias = 30
            
        inicio = poderWon(numeroDias, productos) 
        datos = inicio.logica()
        data={
            "codRes": "00",
            "tienda": tienda,
            "creador": creador,
            "title": title,
            "detalle": "éxito",
            "data": datos
        }
        return data
    elif tipo == 2:
        print("es tipo 2", tipo)
        json = request.get_json()
        producto = json["nombreProducto"]
        categoria = json["categoria"]
        numeroDias = json["numeroDias"]
        inicio = reporteTipo2( producto, categoria) 
        datos = inicio.logica()
        print("datos", datos)
        data={
            "codRes": "00",
            "detalle": "éxito",
            "data": datos
        }
        return data
    elif tipo == 3:
        print("es tipo 3", tipo)
        json = request.get_json()
        producto = json["nombreProducto"]
        categoria = json["categoria"]
        inicio = reporteTipo3( producto, categoria) 
        datos = inicio.logica()
        print("datos", datos)
        data={
            "codRes": "00",
            "detalle": "éxito",
            "data": datos
        }
        return data
    else:
        return "tipo incorrecto"


@app.route('/catalogos/<int:tipo>', methods=[ 'POST'])
def catalogos(tipo):
    if tipo == 1:
        json = request.get_json()
        colecciones = json["colecciones"]
        categorias = json["categorias"]
        try:
            instancia = getCatalogos(colecciones, categorias) 
            data = instancia.logica()
            response = {
                "codRes": "00",
                "data": data
                }
            return response
        except:
            return { "codRes": "99", "data": "error interno" }
    if tipo == 2:
        print("tipo 2")
        json = request.get_json()
        colecciones = json["colecciones"]
        categorias = json["categorias"]
        try:
            instancia = getCatalogos(colecciones, categorias) 
            data = instancia.logica2()
            response = {
                "codRes": "00",
                "data": data
                }
            return response
        except:
            return { "codRes": "99", "data": "error interno" }
    else:
        print("tipo incorrecto")
        return { "codRes": "99", "data": "tipo incorrecto" }


@app.route('/datosCanasta/<int:idCanasta>', methods=[ 'GET'])
def datosCanasta(idCanasta):
    print(idCanasta)
    try:
        instancia = getCatalogos("bolsaProductos", idCanasta) 
        data = instancia.busquedaId()
        response = {
            "codRes": "00",
            "data": data
            }
        return response
    except:
        return { "codRes": "99", "data": "error interno" }
    

@app.route('/registrarBolsa/<int:tipo>', methods=[ 'POST'])
def registrarBolsa(tipo):
    if tipo == 1:
        json = request.get_json()
        try:
            print("registrarBolsa")
            instancia = usuarios(json) 
            data = instancia.logica()
            if data:
                response ={
                    "codRes": "00",
                    "data": "correct"
                }
                return response
            else:
                response = {
                    "codRes": "99",
                    "data": "incorrect"
                }
                return response
        except:
            return { "codRes": "99", "data": "error interno" }
    if tipo == 2:
        print("tipo 2")
        # json = request.get_json()
        # colecciones = json["colecciones"]
        # categorias = json["categorias"]
        try:
            print("")
            # instancia = getCatalogos(colecciones, categorias) 
            # data = instancia.logica2()
            # response = {
            #     "codRes": "00",
            #     "data": data
            #     }
            # return response
        except:
            return { "codRes": "99", "data": "error interno" }
    else:
        print("tipo incorrecto")
        return { "codRes": "99", "data": "tipo incorrecto" }


@app.route('/insertProductos/<int:tipo>', methods=[ 'POST'])
def insertProductos(tipo):
    if tipo == 1:
        json = request.get_json()
        try:
            instancia = usuarios(json) 
            print("json", json)
            data = instancia.logicaUpdate()
            if data:
                response ={
                    "codRes": "00",
                    "data": "correct"
                }
                return response
            else:
                response = {
                    "codRes": "99",
                    "data": "incorrect"
                }
                return response
        except:
            return { "codRes": "99", "data": "error interno" }
    if tipo == 2:
        print("tipo 2")
        # json = request.get_json()
        # colecciones = json["colecciones"]
        # categorias = json["categorias"]
        try:
            print("")
            # instancia = getCatalogos(colecciones, categorias) 
            # data = instancia.logica2()
            # response = {
            #     "codRes": "00",
            #     "data": data
            #     }
            # return response
        except:
            return { "codRes": "99", "data": "error interno" }
    else:
        print("tipo incorrecto")
        return { "codRes": "99", "data": "tipo incorrecto" }


@app.route('/resumen/<int:tipo>', methods=[ 'POST'])
def resumen(tipo):
    if tipo == 1:
        json = request.get_json()
        try:
            instancia = resumenRep(json) 
            data = instancia.logica()
            if data:
                response ={
                    "codRes": "00",
                    "data": data["producto"],
                    "dataDolar": data["dolar"]
                }
                return response
            else:
                response = {
                    "codRes": "99",
                    "data": "null"
                }
                return response
        except:
            return { "codRes": "99", "data": "error interno" }
    if tipo == 2:
        print("tipo 2")
        # json = request.get_json()
        # colecciones = json["colecciones"]
        # categorias = json["categorias"]
        try:
            print("")
            # instancia = getCatalogos(colecciones, categorias) 
            # data = instancia.logica2()
            # response = {
            #     "codRes": "00",
            #     "data": data
            #     }
            # return response
        except:
            return { "codRes": "99", "data": "error interno" }
    else:
        print("tipo incorrecto")
        return { "codRes": "99", "data": "tipo incorrecto" }



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)