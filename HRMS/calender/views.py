from django.shortcuts import render
from django.views.generic import TemplateView


class CalenderView(TemplateView):
    template_name = 'calender/calender.html'
