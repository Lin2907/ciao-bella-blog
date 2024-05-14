from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]