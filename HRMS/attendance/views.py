import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import Attendance


class AttendanceView(TemplateView):
    template_name = 'attendance/attendance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Attendance.objects.all()
        print(context['data'])
        return context


class ClockInOut(View):
    def post(self, request):
        today = datetime.datetime.now()
        time = today.strftime("%H:%M:%S")
        date = today.strftime("%Y-%m-%d")
        if not Attendance.objects.filter(date=date):
            data = Attendance(date=date, clock_in=time, status='present')
            data.save()
        else:
            colck_in = Attendance.objects.get(date=date)
            print(colck_in.clock_in)
            data = Attendance(date=date, clock_in=colck_in.clock_in, clock_out=time, status='present')
            data.save()
        return HttpResponseRedirect('/')
