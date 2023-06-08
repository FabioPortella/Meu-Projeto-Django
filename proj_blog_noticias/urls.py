from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app_noticias.urls", namespace="noticias")),
    path('users/', include("users.urls", namespace="users")), 
]
