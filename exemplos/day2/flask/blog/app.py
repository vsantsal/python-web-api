from flask import Flask
from blog.config import configure


def create_app():
    """Cria uma instância do Flask e configura a aplicação."""
    app = Flask(__name__)
    configure(app)
    return app
