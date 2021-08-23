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
            data = Attendance1.objects.get(user=request.user)
            hours = (int(time[:2])-int(str(data.clock_in)[:2]))
            minets = (int(time[3:5])-int(str(data.clock_in)[3:5]))
            print(hours)
            print(minets)
            Attendance1.objects.filter(user=request.user).update(clock_out=time,total_work_duration=f'{hours}:{minets}')

        return HttpResponseRedirect('/')
