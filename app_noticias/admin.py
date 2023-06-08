from django.contrib import admin

from .models import Noticia, Comentario

class ComentarioInline(admin.TabularInline):  # ou use admin.StackedInline para exibir em formato de pilha
    model = Comentario

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    inlines = [ComentarioInline]

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass