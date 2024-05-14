from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from .models import BlogPost, Comment,Tag ,BlogPostTag

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Displays all of blog posts"

class PostList(generic.ListView):
    model = BlogPost
    template_name = 'post_list.html'


class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'post_detail.html'


