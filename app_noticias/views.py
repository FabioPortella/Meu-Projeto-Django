from django.shortcuts import render

from .models import Noticia, Comentario

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

def noticia(request, id):
    template = 'noticias/noticia.html'
    noticia = Noticia.objects.get(id=id)
    comentarios = Comentario.objects.filter(titulo_comentario=id).order_by('-data_comentario')
    context = {
        'noticia': noticia,
        'comentarios': comentarios 
        }
    return render(request, template , context)