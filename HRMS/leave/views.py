from django.shortcuts import render
from .forms import LeaveForm
from django.views.generic.edit import FormView


# Create your views here.
class LeaveView(FormView):
    template_name = 'leave/leave.html'
    form_class = LeaveForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)