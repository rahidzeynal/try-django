"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

# Actually Django acts like MVT(Models Views Templates) system
def home_view(request):
    """
    Take in a request(Django sends request)
    Return HTML as a response(We pick to return the response)
    """

    random_article_id = random.randint(1, 4)

    # Get data from database
    article_obj = Article.objects.get(id=random_article_id)
    article_query_set = Article.objects.all()
    context = {
        "object_list": article_query_set,
        "article_obj": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    # Django Templates
    HTML_STRING = render_to_string('home-view.html', context=context)
    # HTML_STRING = """
    # <h1>{title} (id: {id})</h1>
    # <p>{content}</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)