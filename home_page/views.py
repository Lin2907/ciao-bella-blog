from django.shortcuts import render, get_object_or_404, reverse, redirect
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
    post = get_object_or_404(BlogPost, slug=slug, status=1)
    comments = post.comments.all().order_by("-published_date")
    comment_count = post.comments.count()
    liked = False
    if request.user.is_authenticated:
        liked = LikedPost.objects.filter(post=post, user=request.user)

    # Initialize forms
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment is successfully posted.')
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
            'post': post,
        },
    )


def search_posts(request):

    if request.method == "POST":
        searched = request.POST['searched']
        posts = BlogPost.objects.filter(title__icontains=searched)

    return render(request, 'home_page/search_posts.html',
                  {'searched': searched, 'posts': posts})

# Likes view


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

# 404 and 500 error views


def custom_404(request, exception):
    return render(request, 'home_page/404.html', status=404)


def custom_500(request):
    return render(request, 'home_page/500.html', status=500)


def comment_edit(request, slug, comment_id):
    post = get_object_or_404(BlogPost, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment_form.save()
            messages.success(request, 'Comment updated successfully.')
        else:
            messages.error(request, 'Error updating comment.')

    return redirect('post_detail', slug=slug)


def comment_delete(request, slug, comment_id):
    post = get_object_or_404(BlogPost, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
    else:
        messages.error(request, "You can only delete your own comments.")

    return redirect('post_detail', slug=slug)