from django.contrib import admin
from django.forms import ModelForm
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display =['title','description','language','image']

admin.site.register(Project,ProjectAdmin)
