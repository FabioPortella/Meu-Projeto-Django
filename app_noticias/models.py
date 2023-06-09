from django.db import models
from django.contrib.auth.models import User


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
    

class Comentario(models.Model):
    texto = models.TextField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.texto) > 50:
            return self.texto[:50] + "..."
        else:
            return self.texto