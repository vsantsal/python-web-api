import click

from blog.posts import (
    get_all_posts, 
    get_post_by_slug, 
    update_post, 
    new_post
)

@click.group()
def post():
    """
    Comandos para gerenciar posts.
    """
    pass

@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """
    Cria um novo post.
    
    :param title: Título do post
    :param content: Conteúdo do post
    """
    new = new_post(title, content)
    click.echo(f"Post {new} criado com sucesso!")


def configure(app):
    app.cli.add_command(post)
