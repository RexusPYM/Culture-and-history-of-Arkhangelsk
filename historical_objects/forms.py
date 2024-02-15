from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Mail, HistoricalObject, ProposedHistoricalObject
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm


class EmailForm(forms.ModelForm):
    
    class Meta:
        model = Mail
        fields = ("mail",)
        widgets = {
            "mail": forms.EmailInput(attrs={'id': 'email'})
        }
        labels = {
            "mail": "Email"
        }

    def clean(self):
        mail = self.cleaned_data["mail"]
        if Mail.objects.filter(mail=mail).exists():
            raise forms.ValidationError("Такой адрес электронной почты уже подписан")

        return mail


class HistoricalObjectForm(forms.ModelForm):
    class Meta:
        model = HistoricalObject
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-input'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-input'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-input'}),
        }
        # labels = {
        #     "username": "Логин"
        # }


class ProposeHistoricalObjectForm(forms.ModelForm):
    class Meta:
        model = ProposedHistoricalObject
        fields = ("name", "object_type", "description", "picture")
        labels = {
            "name": "Название объекта",
            "object_type": "Тип объекта",
            "description": "Описание объекта",
            "picture": "Изображение объекта"
        }
