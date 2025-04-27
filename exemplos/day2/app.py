from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    """Ponto de entrada da aplicação"""
    return "<strong>Hello world</strong>"
