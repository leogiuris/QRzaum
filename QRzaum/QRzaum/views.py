from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'QRzaum/index.html')