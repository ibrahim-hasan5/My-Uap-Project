

# Register your models here.
from django.contrib import admin

from .models import Course,fact_and_figures,Prerequisite

# admin.py
from django.contrib import admin

admin.site.register(fact_and_figures)
admin.site.register(Course)
admin.site.register(Prerequisite)
