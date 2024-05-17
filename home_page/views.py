from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from .models import BlogPost, Comment
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Displays all of blog posts"

class PostList(generic.ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'



def post_detail(request, slug):
    
# Will display one post from PostList
    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(BlogPost, slug=slug)

    return render(
        request,
        "home_page/post_detail.html",
        {
            "post": post,
            
        },
    )
