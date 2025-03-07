from pathlib import Path
from database import conn


def get_posts_from_database(post_id = None):
    """Obtém os posts do banco de dados"""
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")

    if post_id:
        results = cursor.execute(f"SELECT * FROM post WHERE id = {post_id};")
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]



def get_post_list(posts):
    """Gera a lista de posts"""
    post_list = [
    f"""<li> <a href='/{post["id"]}'> {post["title"]} </a> </li>"""
    for post in posts
    ]  
    return "\n".join(post_list)


def render_template(template_name, **context):
    """Renderiza um template"""
    template = Path(template_name).read_text()
    return template.format(**context).encode("utf-8")


def application(environ, start_response):
    """Aplicação WSGI"""
    # retorno padrão
    body = b"Content Not Found"
    status = "404 Not Found"

    # processar o request
    path = environ.get("PATH_INFO", "/")
    method = environ.get("REQUEST_METHOD", "GET")

    if path == "/" and method == "GET":
        posts = get_posts_from_database()
        body = render_template(
            "list.template.html",
            post_list=get_post_list(posts)
        )
        status = "200 OK"
    elif path.split("/")[-1].isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render_template(
            "post.template.html",
            post=get_posts_from_database(post_id=post_id)[0]
        )
        status = "200 OK"

    # criar o response

    headers = [("Content-Type", "text/html")]
    start_response(status, headers)

    return [body]
