from django.shortcuts import render

def index(request):
    template = 'noticias/index.html'
    return render(request, template)
