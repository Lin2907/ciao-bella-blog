from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostList.as_view(), name='blogpost_list'),
    path("<slug:slug>/", views.post_detail, name='post_detail'),
    path("search_posts", views.search_posts, name="search_posts"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/like/', views.like_post, name='like_post'),
    path('<slug:slug>/unlike/', views.unlike_post, name='unlike_post'),
]
