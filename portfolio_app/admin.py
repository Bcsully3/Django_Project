from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Student

# Register your models here so they can be edited in admin panel
admin.site.register(Student)
