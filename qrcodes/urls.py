from django.urls.conf import path
from qrcodes import views

app_name = "qrcodes"

urlpatterns = [
    path('lista/', views.QrcodeListView.as_view(),name='lista-qrcodes'),
    path('user/', views.UserQrcodeListView.as_view(),name='lista-userqrcodes'),
    path('create/', views.QrcodeCreateView.as_view(),name='criar-qrcode'),
    path('delete/<int:pk>', views.QrcodeDeleteView.as_view(),name='apaga-qrcode'),
]

