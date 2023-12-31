from django.shortcuts import render, get_object_or_404, redirect
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
        qrcodes = QRCODE.objects.filter(public = True)
        if 'user_id' in kwargs:
            qrcodes = qrcodes.filter(user = User.objects.get(id = kwargs['user_id']))
        for obj in qrcodes:
            obj.img = segno.make(obj.qr_data).png_data_uri(scale = 15)
        contexto = {
            "qrcodes": qrcodes,
            "host": request.get_host(),
        }
        return render(request, "qrcodes/listAll.html", contexto)


class UserQrcodeListView(View):
    def get(self, request, *args, **kwargs):
        qrcodes = QRCODE.objects.filter(user = get_user(request))
        for obj in qrcodes:
            obj.img = segno.make(obj.qr_data).png_data_uri(scale = 12)
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
            new_qrcode.read_count = 0
            new_qrcode.save()
            new_qrcode.qr_data = str(request.get_host()) + "/qrcodes/read/" + str(new_qrcode.id)
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


class QrcodeUpdateView(View):
    def get(self,request,pk,*args, **kwargs):
        qrcode = QRCODE.objects.get(pk=pk)
        formulario = QrcodeModel2Form(instance=qrcode)
        return render(request, 'qrcodes/formQrcode.html', 
                      {"formulario":formulario, "titulo":"Edita um QR Code", "submitText":"Atualizar"})
    
    def post(self, request, pk, *args, **kwargs):
        qrcode = get_object_or_404(QRCODE, pk=pk)
        formulario = QrcodeModel2Form(request.POST, instance=qrcode)
        if formulario.is_valid():
            qrcode = formulario.save() # cria uma pessoa com os dados do formulário
            qrcode.qr_data = str(request.get_host()) + "/qrcodes/read/" + str(qrcode.id)
            qrcode.save() # salva uma pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy("qrcodes:lista-userqrcodes"))
        else:
            print("nao é valido")
            contexto = {'form': formulario, "titulo":"Edita um QR Code", "submitText":"Atualizar"}
            return render(request, 'qrcodes/formQrcode.html', contexto)


class QrcodeDeleteView(View):
    def get(self,request,pk,*args, **kwargs):
        qrcode = QRCODE.objects.get(pk=pk)
        contexto = { 'qrcode': qrcode, }
        return render(  request, 
                        'contatos/apagaContato.html', 
                        contexto)

    def post(self, request, pk, *args, **kwargs):
        qrcode = get_object_or_404(QRCODE, pk=pk)
        qrcode.delete()
        return HttpResponseRedirect(reverse_lazy("qrcodes:lista-userqrcodes"))
    

def QrcodeRedirect(request, pk):
    qrcode = QRCODE.objects.get(pk=pk)
    qrcode.read_count += 1
    qrcode.save()
    url = qrcode.url
    return redirect(url)