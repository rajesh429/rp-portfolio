from django.shortcuts import render, get_object_or_404
from .models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, slug):
    #project = Project.objects.get(pk=pk)
    project = get_object_or_404(Project,slug=slug)
    context = {
        "project": project
    }
    return render(request, 'project_detail.html', context)
