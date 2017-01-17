from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from customer.forms import ContactForm
from django.contrib import messages
from django.conf import settings
import json


# Create your views here.
def home(request):
    form = ContactForm()
    #return render(request, 'home.html', {'form': form})
    return render(request, 'home.html', {})


def success(request):
	return render(request, 'newsletter_success.html', {})



# def home(request):
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
# return render(request, 'home.html', {'form':form})



# def home(request):
# 	form = ContactForm(initial={'email': 'Your Email Address'})
# 	return render(request, 'home.html', {'form':form})

    	