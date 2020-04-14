from django.views.generic import ListView, DetailView

from .models import Post


class BlogPostListView(ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = 'blog/list.html'
    context_object_name = 'blog_posts'


class BlogPostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = 'blog/detail.html'
    context_object_name = 'post'
