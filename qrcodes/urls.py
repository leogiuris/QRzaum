from django.urls.conf import path
from qrcodes import views

app_name = "qrcodes"

urlpatterns = [
    path('lista/', views.QrcodeListView.as_view(),name='lista-qrcodes'),
]

