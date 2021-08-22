from django.urls import path
from .views import CalenderView

urlpatterns = [
    path('calender', CalenderView.as_view(), name='calender'),
]