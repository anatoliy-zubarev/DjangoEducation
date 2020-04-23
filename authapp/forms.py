from django.contrib.auth.models import User
from django import forms
from authapp.models import PizzaShop

class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class PizzShopForm(forms.ModelForm):
    class Meta:
        model = PizzaShop
        fields = ('name', 'logo')