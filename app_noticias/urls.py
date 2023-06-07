from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
]
