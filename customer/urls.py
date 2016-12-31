from django.conf.urls import url, include
from . import views



urlpatterns = [    
    url(r'^send-email/$', views.send_email, name='send_email'),
    ]