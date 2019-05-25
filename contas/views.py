# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    return HttpResponse("Bem vindo")

# view de login
def paginaLogin(request):
    return HttpResponse("Pagina de Login")

def paginaRegistro(request):
    return HttpResponse("Página de Registro")
