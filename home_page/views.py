from django.shortcuts import render,get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic import ListView
from .models import BlogPost, Comment, LikedPost
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
    paginate_by = 6


def post_detail(request, slug):
    
# Will display one post from PostList
    post = get_object_or_404(BlogPost, slug=slug , status=1)
    comments = post.comments.all().order_by("-published_date")
    comment_count = post.comments.filter(approved=True).count()
    liked = False
    if request.user.is_authenticated:
        liked = LikedPost.objects.filter(post=post, user=request.user)

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
            "liked": liked,
            "like_count": post.like_count(),
            
        },
    )
       

def search_posts(request):

        if request.method == "POST":
            searched = request.POST ['searched']
            posts=BlogPost.objects.filter(title__icontains = searched)
            
            return render(
                request, 'home_page/search_posts.html', 
                {'searched':searched ,'posts': posts})


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    
    # Comment delete option

    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment Deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))

    #Likes view

def like_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    user = request.user if request.user.is_authenticated else None

    if user:
        liked_post, created = LikedPost.objects.get_or_create(post=post, user=user)
        messages.success(request, "Post liked!")
    else:
        messages.info(request, "You must be logged in to like a post.")

    return redirect('post_detail', slug=slug)

def unlike_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    user = request.user if request.user.is_authenticated else None

    if user:
        like_post = LikedPost.objects.filter(post=post, user=user)

        if like_post.exists():
            like_post.delete()
            messages.success(request, "Unliked!")
    else:
        messages.info(request, "You must be logged in to unlike a post.")

    return redirect('post_detail', slug=slug)
