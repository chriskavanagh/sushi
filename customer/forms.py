from __future__ import absolute_import
from django import forms
from .models import Customer
#from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ['email']
		widgets = {
			'email': forms.EmailInput(
			 	attrs={'placeholder':'Enter Your Email Address', 'id': 'email_text',
			 									 	'class':'form-control input-lg'}
			 	)
			 }

	def clean_email(self):
		email = self.cleaned_data['email']
		cust_email = Customer.objects.filter(email=email).count()
		if cust_email:
			raise forms.ValidationError("Email Address Already In Use!")
		return email

    