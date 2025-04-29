from flask import Flask


def create_app():
    """Cria uma instância do Flask e configura a aplicação."""
    app = Flask(__name__)
    return app
