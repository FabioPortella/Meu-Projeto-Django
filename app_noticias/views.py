from django.shortcuts import render

from .models import Noticia

def index(request):
    template = 'noticias/index.html'
    return render(request, template)


def noticias(request):
    template = 'noticias/noticias.html'
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    context = {
        'noticias': noticias
        }
    return render(request, template , context)