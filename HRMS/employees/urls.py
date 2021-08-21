from django.urls import path
from .views import EmployeeSearch

urlpatterns = [
    path('employees', EmployeeSearch.as_view(), name='employees'),
]