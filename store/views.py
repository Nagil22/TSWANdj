from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

    
class IndexView(TemplateView):
    template_name = 'store/home.html'
    
    
     
class AboutView(TemplateView):
    template_name = 'store/about.html'
    
    
     
class ProductView(TemplateView):
    template_name = 'store/products.html'
       
    
class ContactView(TemplateView):
    template_name = 'store/contact.html'
    

    
class LoginView(TemplateView):
    template_name = 'store/login.html'
    
    
class SignupView(TemplateView):
    template_name = 'store/signup.html'
    
    
    