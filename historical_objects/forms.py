from django import forms
from django.core.exceptions import ValidationError

from .models import Mail, HistoricalObject
from django.core.validators import validate_email


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
