from django.contrib import messages
from customer.forms import ContactForm
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from customer.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import Http404, HttpResponse
import json



def home(request):
    form = ContactForm()
    return render(request, 'home.html', {'form': form})


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

    	