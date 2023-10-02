from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cadastro
from django.contrib import messages
from django.contrib.messages import constants
from hashlib import sha256


def login(request):
    return render(request, 'login.html')


def cadastrar(request):
    return render(request, 'cadastrar.html')


def valida_cadastro(request):
    email = request.POST.get('email')
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    conf_senha = request.POST.get('conf_senha')
    user = Cadastro.objects.filter(email=email)
    teste = (email, nome, senha, conf_senha)

    try:
        for t in teste:
            if len(t.strip()) == 0:
                messages.add_message(request, constants.ERROR,
                                     "Preencha todos os campos")
                return redirect('/cadastrar/')

        if senha != conf_senha:
            messages.add_message(request, constants.ERROR,
                                 "As senhas estão diferentes")
            return redirect('/cadastrar/')

        if len(user) > 0:
            messages.add_message(request, constants.ERROR,
                                 "Email já cadastrado")
            return redirect('/cadastrar/')

        if len(senha) < 8:
            messages.add_message(request, constants.ERROR,
                                 "Senha menor que 8 caracteres")
            return redirect('/cadastrar/')
        senha = sha256(senha.encode()).hexdigest
        usuario = Cadastro(email=email,
                           nome=nome,
                           senha=senha)
        usuario.save()
        messages.add_message(request, constants.SUCCESS,
                             "Conta Cadastrada com Sucesso!")
        return redirect('/cadastrar/')
    except:
        return redirect('/cadastrar/')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    usuario = Cadastro.objects.filter(email=email).filter(senha=senha)

    if usuario == 0:
        messages.add_message(request, constants.ERROR,
                             "Email ou Senha incorreta!")
        return redirect(request, '/login/')
    if len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
    return redirect(request, '/home/')
