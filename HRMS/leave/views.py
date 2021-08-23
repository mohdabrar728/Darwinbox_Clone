from django.shortcuts import render
from .forms import LeaveForm
from django.views.generic.edit import CreateView


class LeaveView(CreateView):
 form_class = LeaveForm
 template_name = 'leave/leave.html'
 success_url = '/home/'