from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'QRzaum/index.html')

def homeSec(request):
    return render(request,"seguranca/secHome.html")

def registro(request):
    if request == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sec-home')
    else:
        form = UserCreationForm()
        context = { 'form': form,
                    'titulo':'Registro',
                    'tituloPagina':'Registro de Usuário',
                    'textoBotao':'Registro',
                    }
        return render(request,
                            'seguranca/registro.html', context)