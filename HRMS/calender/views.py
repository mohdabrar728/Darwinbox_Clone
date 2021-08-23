from django.shortcuts import render
from django.views.generic import TemplateView


class CalenderView(TemplateView):
    template_name = 'calender/calender.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['time'] = self.request.session['time']
        context['ip'] = self.request.get_signed_cookie('ip', default='Not Detected', salt='ip')
        return context
