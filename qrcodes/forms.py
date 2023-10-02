from django import forms
from qrcodes.models import QRCODE


class QrcodeModel2Form(forms.ModelForm):
    name = forms.CharField(
        label="Nome ",
        widget=forms.TextInput(
            attrs={"class": "w-auto form-control", "placeholder": "Nome"}
        ),
    )
    url = forms.CharField(
        label="Url ",
        widget=forms.TextInput(
            attrs={"class": "w-auto form-control", "placeholder": "URL"}
        ),
        required=True,
    )
    public = forms.BooleanField(
        label="Público ",
        initial=True,
        required=False,
    )
    class Meta:
        model = QRCODE
        fields = ["name","url","public"]


    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='Dê um apelido para este código')
    url = models.CharField(max_length=100, help_text='Para onde este QRCODE leva')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """
