# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    return render(request, "contas/home.html")

# view de login
def paginaLogin(request):
    return render(request, "contas/login.html")

def paginaRegistro(request):
    return render(request, "contas/registro.html")
