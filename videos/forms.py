from django import forms
from django.core.validators import RegexValidator


class UserForm(forms.Form):
    payroll = forms.CharField(
        label="Número de nómina",
        required=True,
        validators=[
            RegexValidator(
                "^[A-Za-z0-9]{10}$",
                message="Nómina en formato incorrecto. Debe capturar solo números y letras.",
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    name = forms.CharField(
        label="Nombre completo",
        max_length=50,
        required=True,
        validators=[
            RegexValidator(
                "^[A-Za-z\s]+$",
                message="Nombre de usuario en formato incorrecto. Debe capturar solo letras.",
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    quantity = forms.IntegerField(
        label="Cantidad de videos",
        required=True,
        validators=[
            RegexValidator(
                "^[0-9]+$",
                message="Cantidad de videos en formato incorrecto. Debe capturar solo números.",
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )


class VideoForm(forms.Form):
    name = forms.CharField(
        label="Nombre del video",
        max_length=50,
        required=True,
        validators=[
            RegexValidator(
                "^[A-Za-z0-9\s]+$",
                message="Nombre del video en formato incorrecto. Debe capturar solo números y letras.",
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    extension = forms.CharField(
        label="Extension del video",
        max_length=5,
        required=True,
        validators=[
            RegexValidator(
                "^\.[A-Za-z0-9]+$",
                message="Extensión del video en formato incorrecto. Debe capturar solo números y letras.",
            )
        ],
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    size = forms.IntegerField(
        label="Tamaño del video",
        required=True,
        validators=[
            RegexValidator(
                "^[0-9]+$",
                message="Tamaño del video en formato incorrecto. Debe capturar solo números",
            ),
            RegexValidator(
                "^[0-3]$",
                message="El archivo no debe pesar más de 3 MB",
            ),
        ],
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
