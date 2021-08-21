from django.shortcuts import render
from django.views.generic import ListView
from .models import Attendance

class AttendanceView(ListView):
    template_name_suffix = ''
    model = Attendance
