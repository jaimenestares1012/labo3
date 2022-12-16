from flask import Flask, request

from flask_cors import CORS
from reporting import reporteTipo1
from reportingtottus import reporteTipo2
from reportingMetro import reporteTipo3

from adquisitivoWon import poderWon
from utils import getCatalogos
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
        numeroDias = json["numeroDias"]
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


@app.route('/catalogos', methods=[ 'POST'])
def catalogos():
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




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)