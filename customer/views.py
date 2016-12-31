from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from .forms import ContactForm
from .models import Customer

from sendgrid.helpers.mail import *
from sendgrid import *
import os

# Create your views here.
def send_email(request):
    if request.is_ajax() and request.POST:
        email = request.POST.get('email')
        cust_email = Customer.objects.filter(email=email).count()
        if cust_email:
            data = {'message': '{} is already registered'.format(email)}
            return JsonResponse(data)
        else:
            data = {'message': '{} is now registered for our newsletter'.format(email)}
            Customer.objects.create(email=email)
            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            to_email = Email('ckava3@gmail.com')
            subject = 'Newsletter'
            from_email = Email('app61490599@heroku.com')
            content = Content("text/plain", "Hello, Email!")
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return JsonResponse(data)
    else:
        raise Http404




# def send_email(request):
#     if request.is_ajax() and request.POST:
#         email = request.POST.get('email')
#         cust_email = Customer.objects.filter(email=email).count()
#         if cust_email:
#             data = {'message': '{} is already registered'.format(email)}
#             return JsonResponse(data)
#         else:
#             data = {'message': '{} is now registered for our newsletter'.format(email)}
#             Customer.objects.create(email=email)
#             to_email = email
#             subject = 'Newsletter'
#             from_email = settings.EMAIL_HOST_USER
#             message = 'You Are Now Signed Up For BenGui-Sushi Newsletter!'
#             send_mail(subject, message, from_email, [to_email,], fail_silently=False)
#             return JsonResponse(data)
#     else:
#         raise Http404





# def send_email(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             email = cd['email']
#             new_email = form.save(commit=True)
#             to_email = form.cleaned_data['email']   # cd['email']
#             subject = 'Newsletter'
#             from_email = settings.EMAIL_HOST_USER
#             message = 'You Are Now Signed Up For BenGui Newsletter!'
#             send_mail(subject, message, from_email, [to_email,], fail_silently=False)
#             return redirect('success')
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form':form})