from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Attendance


class AttendanceView(TemplateView):
    template_name = 'attendance/attendance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Attendance.objects.all()
        print(context['data'])
        return context
