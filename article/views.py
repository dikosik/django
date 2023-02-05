from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница  Article ")
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