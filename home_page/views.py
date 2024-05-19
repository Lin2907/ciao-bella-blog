from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from django.views.generic import ListView
from .models import BlogPost, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib import messages

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
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # Reinitialize the form to be empty after saving the comment
            comment_form = CommentForm()
        else:
            # If the form is not valid, it will be returned with errors
            pass
    else:
        # Initialize an empty form if the request method is not POST
        comment_form = CommentForm()

    return render(
        request,
        "home_page/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            
        },
    )
       

def search_posts(request):

        if request.method == "POST":
            searched = request.POST ['searched']
            posts=BlogPost.objects.filter(title__contains = searched)
            
            return render(
                request, 'home_page/search_posts.html', 
                {'searched':searched ,'posts': posts}) 

