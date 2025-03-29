import cgi
import json
from database import conn

from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader("templates"))

MENSAGEM_OK = "200 OK"

def get_posts_from_database(post_id = None):
    """Obtém os posts do banco de dados"""
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")

    if post_id:
        results = cursor.execute(f"SELECT * FROM post WHERE id = {post_id};")
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]


def render_template(template_name, **context):
    """Renderiza um template"""
    template = env.get_template(template_name)
    return template.render(**context).encode("utf-8")


def add_new_post(post):
    """Adiciona um novo post ao banco de dados"""
    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO post (title, content, author)
        VALUES ('{post["title"]}', '{post["content"]}', '{post["author"]}');"""
    )
    conn.commit()


def application(environ, start_response):
    """Aplicação WSGI"""
    # retorno padrão
    body = b"Content Not Found"
    status = "404 Not Found"
    content_type = "text/html"

    # processar o request
    path = environ.get("PATH_INFO", "/")
    method = environ.get("REQUEST_METHOD", "GET")

    if path == "/" and method == "GET":
        posts = get_posts_from_database()
        body = render_template(
            "list.template.html",
            post_list=posts
        )
        status = MENSAGEM_OK

    elif path == "/api" and method == "GET":
        posts = get_posts_from_database()
        status = MENSAGEM_OK
        body = json.dumps(posts).encode("utf-8") # serialização
        content_type = "application/json"

    elif path.split("/")[-1].isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render_template(
            "post.template.html",
            post=get_posts_from_database(post_id=post_id)[0]
        )
        status = MENSAGEM_OK
    elif path == "/new" and method == "GET":
        body = render_template("form.template.html")
        status = "200 OK"
    elif path == "/new" and method == "POST":
        form = cgi.FieldStorage(
            fp=environ["wsgi.input"],
            environ=environ,
            keep_blank_values=True
        )
        post = {item.name:item.value for item in  form.list}
        add_new_post(post)
        body = b"New Post created with success"
        status = "201 Created"
    # criar o response

    headers = [("Content-Type", content_type)]
    start_response(status, headers)

    return [body]
