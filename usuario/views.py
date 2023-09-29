from django.shortcuts import render, redirect
from .models import Cadastro


def login(request):
    return render(request, 'login.html')


def cadastrar(request):
    return render(request, 'cadastrar.html')


def validação(request):
    email = request.POST.get('email')
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    conf_senha = request.POST.get('conf_senha')
    usuario = Cadastro(email=email,
                       nome=nome,
                       senha=senha)

    usuario.save()

    return redirect('/cadastrar/?status=0')


def recuperar(request):
    return render(request, 'recuperar.html')
