from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    #first_name = forms.CharField(label='Nome', max_length=30)
    #last_name = forms.CharField(label='Sobrenome', max_length=30)
    email = forms.EmailField(label='Email', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
        fields = UserCreationForm.Meta.fields + ('email',)


def logout_view(request):
    """Faz o Log out do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('noticias:index'))


def register(request):
    """Faz o cadastro de um novo usuário"""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = CustomUserCreationForm()
    else:
        # Processa o formulário preenchido
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            # Faz o login do usuário e o redireciona para a página inicial
            autentificacao = authenticate(username=novo_usuario.username, password=request.POST['password1'])
            login(request, autentificacao)
            return HttpResponseRedirect(reverse('noticias:index'))
        
    template = 'users/register.html'
    context = {
        'form': form
    }
    return render(request, template, context)