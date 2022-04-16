
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import linear_model

class algoritmo():
    def __init__(self) :
        print("inicio")

    def algopredictivo(self,abierta,moroso,trabajo):
        print("en el algo predictivo", abierta, moroso, trabajo)

        datos= pd.read_csv("dataentrenada.csv")
        daraframe= pd.DataFrame(datos)

        print(daraframe)

        x = (daraframe[["abierta","moroso","trabajo"]])
        y = (daraframe["resultado"])


        # print(x)
        #entrenamiento

        X_train, X_test, y_train, y_test= train_test_split(x, y, test_size=0.25, random_state=0)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        datanew={
            'abierta':[abierta],
            'moroso':[moroso],
            'trabajo': [trabajo]
        }
        clientesnew=pd.DataFrame(datanew, columns=['abierta', 'moroso', 'trabajo'])
        prediccion=model.predict(clientesnew)
        print(clientesnew)
        print("este es el resultado de la prediccion",prediccion)
        return prediccion

