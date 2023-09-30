from django.urls.conf import path
from qrcodes import views

app_name = "qrcodes"

urlpatterns = [
    path('lista/', views.QrcodeListView.as_view(),name='lista-qrcodes'),
    path('userQRs/', views.UserQrcodeListView.as_view(),name='lista-userqrcodes'),
    path('criarQR/', views.QrcodeCreateView.as_view(),name='criar-qrcode'),
    path("qrcode/<int:pk>", views.qrcode)
]

