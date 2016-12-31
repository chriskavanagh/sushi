from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.EmailField(max_length=70,blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ('email',)

	def __unicode__(self):
		return self.email