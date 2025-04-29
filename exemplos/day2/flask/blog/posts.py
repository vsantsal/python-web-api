from datetime import datetime
from blog.database import mongo


def get_all_posts(published: bool =True):
    """
    Obtém todos os posts do banco de dados.

    :param published: Se True, retorna apenas os posts publicados
    """
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")


def get_post_by_slug(slug: str) -> dict:
    """
    Obtém um post pelo slug.
    
    :param slug: Slug do post
    :return: Post encontrado ou None
    """
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post(slug: str, data: dict) -> dict:
    """
    Atualiza um post no banco de dados.

    :param slug: Slug do post
    :param data: Dados a serem atualizados
    :return: Post atualizado
    """
    # TODO: se o título mudar, atualizar o slug (falhar se existir)
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})

def new_post(title: str, content: str, published: bool = True) -> str:
    """
    Cria um novo post no banco de dados.
    
    :param title: Título do post
    :param content: Conteúdo do post
    :param published: Se o post está publicado ou não
    :return: Slug do post criado
    """
    slug = title.replace("  ", "-").replace("_", "-").lower()
    # TODO: verificar se post com este slug existe
    # TODO: remover acentos do título no slug
    mongo.db.posts.insert_one({
        "title": slug,
        "content": content,
        "published": published,
        "slug": slug,
        "date": datetime.now(),
    })

    return slug
