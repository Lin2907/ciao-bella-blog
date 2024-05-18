from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from django.views.generic import ListView
from .models import BlogPost, Comment
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Displays all of blog posts"

class PostList(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'object_list'


def post_detail(request, slug):
    
# Will display one post from PostList
    post = get_object_or_404(BlogPost, slug=slug , status=1)
    comments = post.comments.all().order_by("-published_date")
    comment_count = post.comments.filter(approved=True).count

    return render(
        request,
        "home_page/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            
        },
    )
