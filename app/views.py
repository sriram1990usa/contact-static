from django.shortcuts import render
from django.views.generic import TemplateView
#from django.views import View

def index(request):
    return render(request, 'app/index.html')

def contact(request):
    return render(request, 'app/contact.html')    
