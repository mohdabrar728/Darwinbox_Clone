from django.shortcuts import render


# Create your views here.
def chat(request):
    return render(request, 'chatbot/chatbot.html', {'time': request.session['time'],
                                                    'ip': request.get_signed_cookie('ip', default='Not Detected',
                                                                                         salt='ip')})
