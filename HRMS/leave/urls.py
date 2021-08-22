from django.urls import path
from .views import LeaveView

urlpatterns = [
    path('leave', LeaveView.as_view(), name='leave'),
]