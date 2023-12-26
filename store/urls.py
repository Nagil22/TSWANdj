#URLS (APPS)
from django.urls import path
from .views import IndexView , ContactView, AboutView, LoginView,SignupView,ProductView


app_name= 'store'

urlpatterns = [
    
    path('', IndexView.as_view(), name= 'index'),
    path('about/', AboutView.as_view(), name= 'about'),
    path('products/', ProductView.as_view(), name= 'products'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('signup/', SignupView.as_view(), name= 'signup'),
    path('contact/', ContactView.as_view(), name= 'contact'),
    
]