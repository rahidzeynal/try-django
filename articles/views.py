from django.shortcuts import render
from .models import Article
# Create your views here.

def article_search_view(request):
    # print(request.GET)
    query_dict = request.GET # this is a dictionary
    
    try:
        query = int(query_dict.get("query")) # <input type="text" name="query"/>
    except:
        query = None
        
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        "object": article_obj,
    }

    return render(request, "articles/search.html", context=context)


def article_create_view(request):
    context = {}

    if request.method == "POST":
        print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(f"Title is {title} and content is {content}")
        article_obj = Article.objects.create(title=title, content=content)
        context['object'] = article_obj
        context['created'] = True
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }

    return render(request, "articles/detail.html", context=context)