from django.contrib import admin

from .models import Career

class CareerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'level']
    filter_vertical = ['level']

admin.site.register(Career)
