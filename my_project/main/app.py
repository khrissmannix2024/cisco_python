from flask import Flask
from config import SECRET_KEY  # Importar la clave secreta
from main.models import db  # Importar la base de datos y modelos
import sys
import os

# Agregar la carpeta raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config 

app = Flask(__name__)  # Primero se crea la app

# Establecer el modo de desarrollo
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

app.config.from_object(config)  # Cargar la configuración
app.secret_key = SECRET_KEY  # Asignar la clave secreta después

db.init_app(app)  # Inicializar SQLAlchemy

# Crea la base de datos si no existe
with app.app_context():
    db.create_all()

from main import routes  # Importar las rutas después de inicializar la app

if __name__ == '__main__':
    app.run(debug=True)
