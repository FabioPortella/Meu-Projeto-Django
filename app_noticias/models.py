from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=150)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
    

class Comentario(models.Model):
    texto_comentario = models.TextField()
    titulo_comentario = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    autor_comentario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(auto_now_add=True)