from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

# list all posts
class ListPosts(generic.ListView):
    model = Post
    template_name = 'basic_forms/posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all()

# getting started test page
def hello(request):
    return render(request, 'basic_forms/hello.html', {})