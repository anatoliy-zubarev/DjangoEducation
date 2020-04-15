from django.shortcuts import render
from django.views.generic.dates import MonthArchiveView

# Create your views here.

def home(request, month, year):
    return render(request, 'home.html', {})

