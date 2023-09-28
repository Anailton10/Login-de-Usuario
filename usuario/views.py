from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario


def login(request):
    return render(request, 'login.html')


def cadastrar(request):
    return render(request, 'cadastrar.html')


def validação(request):
    email = request.POST.get('email')
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')


def recuperar(request):
    return render(request, 'recuperar.html')
