from .models import BlogPost

def get_article_by_id(id):
    try:
        article = BlogPost.objects.get(id=id)
        return article
    except BlogPost.DoesNotExist:
        return None