from django.contrib import admin
from .models import MenuItem, MenuCategory

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
	list_display = ['category', 'name', 'price', 'description', 'active']

	class Meta:
		model = MenuItem

		
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuCategory)