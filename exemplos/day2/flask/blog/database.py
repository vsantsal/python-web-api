from flask_pymongo import PyMongo


mongo = PyMongo()


def configure(app):
    """Configurar o PyMongo com a aplicação Flask."""
    mongo.init_app(app)
