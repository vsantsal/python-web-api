import click

from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    update_post_by_slug,
    new_post
)


@click.group()
def post():
    """
    Comandos para gerenciar posts.
    """


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """
    Cria um novo post.
    
    :param title: Título do post
    :param content: Conteúdo do post
    """
    resultado = new_post(title, content)
    click.echo(f"Post {resultado} criado com sucesso!")


@post.command("list")
def _list():
    """Lista os posts."""
    for postagem in get_all_posts():
        click.echo(postagem)


@post.command()
@click.argument("slug")
def get(slug):
    """Obtém um post pelo slug."""
    resultado = get_post_by_slug(slug)
    click.echo(resultado or "post not found")


@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published, title):
    """Atualiza um post existente."""
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    update_post_by_slug(slug, data)
    click.echo("Post updated")


# TODO: Adicionar comando para despublicar postagem

def configure(app):
    """Configura o CLI do Flask para o blog."""
    app.cli.add_command(post)
