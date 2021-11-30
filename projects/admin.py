from django.contrib import admin
from django.forms import forms

from projects.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display =['title','description','technology','image']
admin.site.register(Project,ProjectAdmin)
