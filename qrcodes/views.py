from django.shortcuts import render, get_object_or_404
from qrcodes.models import QRCODE
from django.views.generic.base import View
from django.contrib.auth import get_user,get_user_model
from django.core.files import File
from django.db.models import Count
from accounts.models import User
import io
import segno
# from qrcodes.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from qrcodes.forms import QrcodeModel2Form
from qrcodes.qrcode_utils import make_qr
from django.core.files.base import ContentFile
# Create your views here.


class QrcodeListView(View):
    def get(self, request, *args, **kwargs):
        qrcodes = QRCODE.objects.all()
        for obj in qrcodes:
            obj.img = segno.make(obj.url).png_data_uri(scale = 6)
        contexto = {
            "qrcodes": qrcodes,
            "host": request.get_host(),
        }
        return render(request, "qrcodes/listAll.html", contexto)


class UserQrcodeListView(View):
    def get(self, request, *args, **kwargs):
        qrcodes = QRCODE.objects.filter(user = get_user(request))
        for obj in qrcodes:
            obj.img = segno.make(obj.url).png_data_uri(scale = 6)
        contexto = {
            "qrcodes": qrcodes,
        }
        return render(request, "qrcodes/listUserQR.html", contexto)


class QrcodeCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {
            "formulario": QrcodeModel2Form,
            "titulo": "Cria um QR Code",
            "submitText": "Criar QR Code",
        }
        return render(request, "qrcodes/formQrcode.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = QrcodeModel2Form(request.POST)
        if formulario.is_valid():
            new_qrcode = formulario.save(commit=False)
            new_qrcode.user = get_user(request)
            new_qrcode.save()
            new_qrcode.qr_data = str(request.get_host()) + "/" + str(new_qrcode.id)
            new_qrcode.save()
            return HttpResponseRedirect(reverse_lazy("qrcodes:lista-userqrcodes"))
        return render(
            request,
            "qrcodes/formQrcode.html",
            {
                "formulario": formulario,
                "titulo": "Cria um Contato",
                "submitText": "Criar Contato",
            },
        )

class QrcodeDeleteView(View):
    def get(self,request,pk,*args, **kwargs):
        qrcode = QRCODE.objects.get(pk=pk)
        contexto = { 'pessoa': qrcode, }
        return render(  request, 
                        'contatos/apagaContato.html', 
                        contexto)

    def post(self, request, pk, *args, **kwargs):
        print("AAAAA")
        qrcode = get_object_or_404(QRCODE, pk=pk)
        qrcode.delete()
        return HttpResponseRedirect(reverse_lazy("qrcodes:lista-userqrcodes"))