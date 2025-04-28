from flask import Flask, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['APP_NAME'] = 'Meu Blog'
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = PyMongo(app)


@app.route("/")
def index():
    """Ponto de entrada da aplicação"""

    posts = mongo.db.posts.find() # generator

    content_url = url_for("read_content", title="Novidades de 2025")
    return (
        f"<h1>{app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Novidades de 2025</a>"
        "<hr>"
        f"{list(posts)}"
    )


@app.errorhandler(404)
def not_found_page(error):
    """Página de erro 404"""
    return f"<strong>Page not found on {app.config['APP_NAME']}</strong>", 404


def read_content(title):
    """Lê o conteúdo de um artigo"""
    index_url = url_for("index")
    return f"<h1>{title}</h1> <a href='{index_url}'>Voltar</a>"


app.add_url_rule("/<title>", view_func=read_content)
