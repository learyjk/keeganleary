from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Project


def index(request):
    projects = Project.objects.all().order_by('-id')

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/detail.html', context)
