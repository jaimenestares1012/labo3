from flask import Flask, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def inicio():
    return {"message": "proyectoModificado"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)