from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='login'),
    path('test', views.user_logout, name='logout'),
]