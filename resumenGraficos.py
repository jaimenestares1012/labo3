from pymongo import MongoClient
from datetime import datetime, timedelta
import matplotlib.pyplot as pl
import json
import base64
import time
from os import remove

client = MongoClient("mongodb+srv://user_jaime:XhA7pqTDWKfQy6Nh@micluster.pns9q58.mongodb.net")
db  = client.get_database("catalogos")
db2  = client.get_database("tesis-won")




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
        id = col.find().limit(25)
        return id
    except NameError:
        print("ERROR")
        print(NameError)
    print("buscat")


def BuscarMongo2(coleccion ,valor):
    col = db2[coleccion]
    try:
        id = col.find_one({"nombre": valor})
        return id
    except NameError:
        print("ERROR")
        print(NameError)
    print("buscat")

class resumenRep():
    def __init__(self, json):
        self.json = json

    


    def logica(self):
        pl.figure(figsize=(16,4))
        print("logica")
        res = BuscarMongo("variacionDolar")
        arrayDolar = []
        arrayFechasDolar = []
        for b in list(res):
            mien2 = b["Fecha"].replace(".2022", "")
            arrayDolar.append(round(float(b["Último"].replace("," , ".")), 2))
            temp = mien2.replace(".", "-").split("-")
            fechaModificadad = temp[1] + "-" + temp[0]
            arrayFechasDolar.append(fechaModificadad)
        print("-")
        print("-")
        print("arrayDolar", arrayDolar, len(arrayDolar))
        print("arrayFechasDolar", arrayFechasDolar, len(arrayFechasDolar))

        pl.plot(arrayFechasDolar, arrayDolar ,  'b--o')
        pl.title("Variación del dólar")
        pl.xlabel("Día - Mes")
        pl.ylabel("Precio (S/)")
        pl.savefig("dataDolar")

        print("FIN IMAGEN ---- DOLAR")
        arrayGlobal = []
        arrayFechas = []
        for a in self.json["data"]:
            mien = a["fecha"].replace("2022-", "")
            arrayGlobal.append(a["montoTotal"])
            arrayFechas.append(mien)
        pl.figure(figsize=(16,4))
        pl.plot(arrayFechas, arrayGlobal,  'b--o')
        pl.title("Variación de la canasta")
        pl.xlabel("Día - Mes")
        pl.ylabel("Costo total (S/)")
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




    def reporteMef(self):
        fechasDisponibles = []
        i = 0
        dias = int(26)
        print("logica")
        res = BuscarMongo("variacionDolar")
        arrayDolar = []
        arrayFechasDolar = []
        for b in list(res):
            mien2 = b["Fecha"]
            temporal =  b["% var"]
            temp = mien2.replace(".", "-").split("-")
            fechaModificadad = temp[2] + "-" + temp[1] + "-" + temp[0] 
            datos = {
                fechaModificadad: temporal[""]
            }
            # arrayDolar.append(round(float(b["Último"].replace("," , ".")), 2))
           
            
            arrayFechasDolar.append(datos)

        print("arrayFechasDolar", arrayFechasDolar)
        while i <= dias:
            fechaDateTime = datetime.now() - timedelta(i)
            fechaExtraccion = fechaDateTime.strftime("%Y-%m-%d %H:%M:%S") 
            fechaExtraccion2 = fechaExtraccion.split(" ")
            fechaExtraccionclean = fechaExtraccion2[0]
            fechasDisponibles.append(fechaExtraccionclean)
            i = i + 1
        data = []
        fechasDisponibles = fechasDisponibles[::-1]
        dataGlobal =  []
        
        for a in self.json["productosList"]:
            print("<-----------  Inicio iter------->")
            # arrayPrecios = []
            # print("a", a)
            busquedaProductos = BuscarMongo2(a["typeCategory"], a["prod"])
            precioAnterior = 1
            precioInicial = ""
            for fecha in fechasDisponibles:
               
                try:
                    precioNuevo=busquedaProductos[fecha]
                    precioNuevo = precioNuevo.split("S/")
                    precioNuevo = precioNuevo[1].replace(" ", "")
                    if "x" in precioNuevo:
                        precioRoto = precioNuevo.split("x")
                        precioNuevo = precioRoto[0]
                    else:
                        precioNuevo = float(precioNuevo)
                    
                    variacionp = ((precioNuevo - precioAnterior)/precioAnterior)*100
                    variacionc = (precioNuevo - precioAnterior)
                    nombreNuevoP=fecha+"varP"
                    nombreNuevoC=fecha+"varC"
                    busquedaProductos[nombreNuevoP] = variacionp
                    busquedaProductos[nombreNuevoC] = variacionc
                    precioAnterior = precioNuevo
                except:
                    # precioAnterior = precioNuevo
                    # print("No existe data de esta fecha")
                    pass
            
            # print("busquedaProductos]", busquedaProductos)
            busquedaProductos["cantidad"] = a["cantidad"]
            data.append(busquedaProductos)


        print(" FIN-----> siguiente paso")

        dataxdiaGlobal =[]
        sumaTotalDiaAnterior = 1
        for a in fechasDisponibles:
            print("<----------------------------->")
            print("Fecha", a)
            print("<----------------------------->")
            dataxdia =[]
            contador = len(data)
            it = 1
            suma = 0
            for b in data:
                try:
                    price = b[a]
                    price = price.split("S/")
                    precioLimpio = price[1].replace(" ", "")
                    if "x" in precioLimpio:
                        precioRoto = precioLimpio.split("x")
                        precioLimpio = precioRoto[0]
                    else:
                        precioLimpio = float(precioLimpio)
                    sumaParcial = int(b["cantidad"]) * float(precioLimpio)
                    variacionP = 0.0
                    variacionP = 0.0
                    try:
                        campo1 = a+"varP"
                        campo2 = a+"varC"
                        variacionP = b[campo1]
                        variacionC = b[campo2]
                    except:
                        variacionP = 0.0
                        variacionC = 0.0
                    background = ""
                    if  variacionC < 0:
                        background = "#D6EAD6"
                    elif variacionC == 0  :
                        background = ""
                    else:
                        background= "#D97F74"
                    datos = {
                        "producto": b["nombre"],
                        "url": b["url"],
                        "precio": precioLimpio,
                        "cantidad": b["cantidad"],
                        "sumaParcial": round(sumaParcial, 2),
                        "background": background,
                        "variacionPorcentual": round(variacionP, 2),
                        "variacionMonetariaProducto": round(variacionC, 2),
                        "variacionMonetariaSubTotal": round(variacionC * float(b["cantidad"]), 2)
                    }
                    suma = suma + round(sumaParcial, 2)
                    dataxdia.append(datos)
                    datos = {}
                except:
                    datos = {}
                



                dataParcial = {
                    "fecha": a,
                    "montoTotal": round(suma, 2),
                    "numeroProductos": len(dataxdia),
                    "productosXFecha":dataxdia
                }
                
                
                
                
                if len(dataParcial["productosXFecha"])> 0 and contador == it:
                    try:
                        # print("Insert data", b)
                        variacion2p = ((dataParcial["montoTotal"] - sumaTotalDiaAnterior)/sumaTotalDiaAnterior)*100
                        variacion2c = (dataParcial["montoTotal"] - sumaTotalDiaAnterior)
                        dataParcial["varPorcentual"] = round(variacion2p, 2)
                        dataParcial["varMonetario"] = round(variacion2c, 2)
                        background2 = ""
                        if  variacion2c < 0:
                            background2 = "#D6EAD6"
                        elif variacion2c == 0  :
                            background2 = ""
                        else:
                            background2= "#D97F74"
                        dataParcial["background"] = background2
                        sumaTotalDiaAnterior = dataParcial["montoTotal"]


                        variacion = ""
                        for f in arrayFechasDolar:
                            try:
                                variacion = f[a]
                                print("variacio", variacion)
                            except:
                                print("no es")


                        background3 = ""
                        try:
                            if  float(variacion.replace("%", "").replace(",", ".")) < 0:
                                background3 = "#D6EAD6"
                            elif float(variacion.replace("%", "").replace(",", ".")) == 0  :
                                background3 = ""
                            else:
                                background3= "#D97F74"
                        except:
                            pass


                        dataParcial["variacionDolar"] = variacion.replace("%", "")
                        dataParcial["variacionDolarBackground"] = background3
                        dataxdiaGlobal.append(dataParcial)
                        
                    except:
                        print("NOS FUIMOS A LA MIRD")
                dataParcial = {}
                it = it + 1         
        
        
        # for d in dataxdiaGlobal
        # fechasDisponibles = fechasDisponibles[::-1]
        return dataxdiaGlobal[::-1]
