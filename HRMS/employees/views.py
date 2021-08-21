from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EmployeeDetailsForms
from .models import EmployeeDetails


# Create your views here.

class EmployeeSearch(TemplateView):
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmployeeDetailsForms
        return context

    def post(self, request):
        data = EmployeeDetails.objects.get(name=request.POST.get('search_by_employee_name'))
        return render(request,'employees.html', {'form': EmployeeDetailsForms, 'data': data})
