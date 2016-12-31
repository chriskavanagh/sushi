from __future__ import unicode_literals
from django.db import models


# Create your models here.
class MenuCategory(models.Model):
	category = models.CharField('categories', max_length=120)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['category']
		verbose_name_plural = 'menu categories'

	def __unicode__(self):
		return self.category
		

class MenuItem(models.Model):
	category = models.ForeignKey(MenuCategory)
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.CharField(max_length=120)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['name', 'price', 'description']

	@property
	def ItemPrice(self):
		return self.price

	def __unicode__(self):
		return self.name
