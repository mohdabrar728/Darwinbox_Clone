from django.shortcuts import render
from .forms import LeaveForm
from django.views.generic.edit import CreateView
from .models import LeaveModel
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# class LeaveView(CreateView):
#  form_class = LeaveForm
#  template_name = 'leave/leave.html'
#  success_url = '/home/'

def leaveView(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        select_leave_type = request.POST.get('select_leave_type')
        start_date_from = request.POST.get('start_date_from')
        start_date_to = request.POST.get('start_date_to')
        message = request.POST.get('message')
        attachment = request.POST.get('attachment')
        data = LeaveModel(user=request.user, select_leave_type=select_leave_type, start_date_from=start_date_from,
                          start_date_to=start_date_to,
                          message=message, attachment=attachment)
        data.save()
        messages.success(request, f'{request.user} your leave got applied successfully')
        send_mail(
            f"{request.user} has applied for the {select_leave_type}",
            f'{message}',
            settings.EMAIL_HOST_USER,
            ['mohdabrar21140@gmail.com']
        )
    form = LeaveForm
    return render(request, 'leave/leave.html',
                  {'form': form, 'ip': request.get_signed_cookie('ip', default='Not Detected', salt='ip'),
                   'time':request.session['time']})
