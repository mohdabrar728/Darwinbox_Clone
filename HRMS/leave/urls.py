from django.urls import path
from .views import leaveView

urlpatterns = [
    path('leave', leaveView, name='leave'),
]