import os
from dynaconf import FlaskDynaconf


_AQUI = os.path.dirname(os.path.abspath(__file__))

def configure(app):
    """Configurar a aplicação Flask com o Dynaconf."""
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=_AQUI)
