from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EmployeeDetailsForms
from .models import EmployeeDetails
from django.contrib import messages


# Create your views here.

class EmployeeSearch(TemplateView):
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmployeeDetailsForms
        context['time'] = self.request.session['time']
        context['ip'] = self.request.get_signed_cookie('ip', default='Not Detected', salt='ip')
        return context

    def post(self, request):
        name = request.POST.get('search_by_employee_name').title()
        data = EmployeeDetails.objects.filter(name__contains=name)
        if not data:
            messages.info(request, f'Employee Name "{name}" Not Found in Directory')
        print(data)
        return render(request, 'employees.html', {'form': EmployeeDetailsForms, 'data': data})
