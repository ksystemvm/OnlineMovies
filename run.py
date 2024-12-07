# Import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

# Instancias
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# Rutas
@app.route('/')
def inicio():
    return ('Página de Inicio')

# Run
if __name__ == '__main__':
    app.run(debug=True)