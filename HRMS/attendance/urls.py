from django.urls import path
from .views import AttendanceView, ClockInOut
urlpatterns = [
    path('attendance', AttendanceView.as_view(), name='attendance'),
    path('clockinout', ClockInOut.as_view(), name='clockinout')
]