from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostList.as_view(), name='blogpost_list'),
    path("<slug:slug>/", views.post_detail, name='post_detail'),
]