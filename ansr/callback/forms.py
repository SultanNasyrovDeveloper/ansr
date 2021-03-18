from django import forms

from .models import Callback


class CallbackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'login-form-modal-username', 'placeholder': 'Введите имя...'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control phone-input', 'placeholder': 'Введите номер'}))

    class Meta:
        model = Callback
        exclude = ('created', )
