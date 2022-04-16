
from flask import Flask, request

from logica import algoritmo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def inicio():
    return "Inicio"






@app.route('/reporte/prediccion', methods=['POST'])
def prediccion():
    try:
         
        json1 = request.get_json()  
        print("este es mi json", json1)
        abierta=json1["creditoAbierto"]
        moroso=json1["moroso"]
        trabajo=json1["trabajo"]
        result = algoritmo().algopredictivo(abierta,moroso,trabajo)
        print( type(result))
        result2=int(result)
        print( type(result2))
        if result2 ==1:
            return {
                "codRes": "00",
                "message": "Credito Aprobado"
            }
        else:
            return {
                "codRes": "00",
                "message": "Credito Rechazado"
            }

    except:
          return {
            "codRes": "99",
            "message": "Error Controlado"
        }



if __name__ == "__main__":
    app.run()