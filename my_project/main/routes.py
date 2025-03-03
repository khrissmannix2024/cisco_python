from flask import Blueprint
from main.app import app
from main.controllers import index, register

app.route("/", methods=["GET"])(index)
app.route("/register", methods=["GET", "POST"])(register)

# Ruta para evitar el error 404 de favicon.ico
@app.route('/favicon.ico')
def favicon():
    return "", 204  # Responde sin contenido, para evitar el error 404