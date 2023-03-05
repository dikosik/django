from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'article/index.html')


def about(request):
    return render(request, 'article/about.html')
def categories(request, catid):
    if request.POST:
     print(request.POST)
    return HttpResponse(f"<h1> Статьи по категориям <h1><p>{catid}</p>")


def archive(request, year):
   if int(year) > 2020:
       return redirect ('home', permanent=True)
   return HttpResponse(f"<h1> Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> страница не найдена </h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Article, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.style_id,
    }

    return render(request, 'article/post.html', context=context)

def show_category(request, style_id):
    posts = Article.objects.filter(style_id=style_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': style_id,
    }

    return render(request, 'article/index.html', context=context)