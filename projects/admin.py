from django.contrib import admin
from django.forms import forms

from projects.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    # title = forms.CharField(max_length=100)
    # description = forms.TextField()
    # technology = forms.CharField(max_length=20)
    # image = forms.FilePathField(path="/img")
    fields = ('title','description','technology','image')
admin.site.register(Project,ProjectAdmin)
