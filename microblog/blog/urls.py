from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreate.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
