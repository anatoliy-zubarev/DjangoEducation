from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authapp.forms import UserForm, PizzShopForm

# Create your views here.
def home(request):
    return redirect(authapp_home)

@login_required(login_url='login/')
def authapp_home(request):
    return render(request, 'authapp/home.html', {})

def authapp_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzShopForm()
    return render(request, 'authapp/sign_up.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form,
    })