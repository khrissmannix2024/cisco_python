from flask import Flask
from main.models import db  # Importa la base de datos y los modelos
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Agrega my_project al path

import config

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)  # Inicializa SQLAlchemy con la app

@app.route('/')
def home():
    return "<h2>¡Hola, Flask está funcionando!</h2>"

# Crea la base de datos si no existe
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
