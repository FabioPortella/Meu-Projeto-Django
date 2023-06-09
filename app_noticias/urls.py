from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:id>', views.noticia, name='noticia'),
    path('autores/', views.autores, name='autores'),
    path('autores/<int:id>', views.autor, name='autor'),
]
