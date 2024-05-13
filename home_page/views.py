from django.shortcuts import render
from django.views import generic
from .models import BlogPost, Comment,Tag ,BlogPostTag

# Create your views here.
class PostList(generic.ListView):
# Displays all of blog posts"

    model = BlogPost
    template_name = "index.html"



