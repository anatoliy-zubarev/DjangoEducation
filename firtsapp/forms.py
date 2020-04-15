from django import forms
from firtsapp.models import Order
from firtsapp.models import Pizza

class OrderForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Order
        fields = ('pizza', 'name', 'phone')