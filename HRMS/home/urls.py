from django.urls import path
from .views import Home,setcookie

urlpatterns = [
    path('home', setcookie, name='home'),
    path('mainhome', Home.as_view(), name='mainhome')
]