from django.shortcuts import render, get_object_or_404
from qrcodes.models import QRCODE
from django.views.generic.base import View
# from qrcodes.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

class QrcodeListView(View):
    def get(self, request, *args, **kwargs):
        qrcodes = QRCODE.objects.all()
        contexto = { 'qrcodes': qrcodes, }
        return render(request,'qrcodes/listAll.html',contexto)