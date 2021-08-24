import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import Attendance1


class AttendanceView(TemplateView):
    template_name = 'attendance/attendance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Attendance1.objects.filter(user=self.request.user)
        context['time'] = self.request.session['time']
        context['ip'] = self.request.get_signed_cookie('ip', default='Not Detected', salt='ip')
        return context


class ClockInOut(View):
    def post(self, request):
        today = datetime.datetime.now()
        time = today.strftime("%H:%M:%S")
        date = today.strftime("%Y-%m-%d")
        if not Attendance1.objects.filter(user=request.user, date=date):
            data = Attendance1(user=request.user, date=date, clock_in=time, status='present')
            data.save()
        else:
            data = Attendance1.objects.filter(user=request.user, date=date)
            for i in data:
                data = i
            main = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(time[0:2]), int(time[3:5]), int(time[6:8]))-datetime.datetime.combine(data.date,data.clock_in)
            Attendance1.objects.filter(user=request.user, date=date).update(clock_out=time,total_work_duration=main)

        return HttpResponseRedirect('/')
