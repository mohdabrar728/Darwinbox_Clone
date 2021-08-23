from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView
from datetime import datetime, timedelta
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

def setcookie(request):
 reponse = HttpResponseRedirect('mainhome')
 reponse.set_signed_cookie('ip', IPAddr, salt='ip', expires=datetime.utcnow()+timedelta(days=2))
 return reponse

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        # context['time'] = self.request.session.get('time', datetime.now())
        self.request.session['time'] = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        context['time'] = self.request.session['time']
        context['ip'] = self.request.get_signed_cookie('ip', default='Not Detected', salt='ip')
        return context