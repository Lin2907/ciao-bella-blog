from django.shortcuts import render
from django.views import generic
from .models import BlogPost, Comment,Tag ,BlogPostTag

# Create your views here.
class PostList(generic.ListView):
    model = BlogPost
    template_name = "home_page/post_list.html"
