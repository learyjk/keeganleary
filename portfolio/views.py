from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Project
from blog.models import Post


def index(request):
    projects = Project.objects.all().order_by('-id')[:3]
    blog_posts = Post.objects.all()[:2]

    context = {
        'projects': projects,
        'blog_posts': blog_posts
    }

    return render(request, 'portfolio/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/detail.html', context)


def projects(request):
    projects = Project.objects.all().order_by('-id')

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/projects.html', context)
