from django.urls import path
from .views import (
    PostsListView,
    AboutView,
    ContactViev,
    DetailView,
    SearchView,
    CreatePostView,
    UpdatePostView,
    DeletePostView,
CommentCreateView,
    CategoryPostView,
    LikePostView,
    CommentCreateView,
    CategoryPostView,
    LikePostView,

CommentCreateView
    )

app_name = 'blog'

urlpatterns = [
    path('', PostsListView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactViev.as_view(), name='contact'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('post/new/', CreatePostView.as_view(), name='post_create'),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('post/comment/', CommentCreateView.as_view(), name='post_comment'),
    path('categories/<int:pk>/posts', CategoryPostView.as_view(), name='category_posts'),
    path('like-post/<int:pk>/', LikePostView.as_view(), name='like-post'),
    path('post/comment/', CommentCreateView.as_view(), name='comment'),
    # path('post/comment/', CommentCreateView.as_view(), name='post_comment'),
    # path('categories/<int:pk>/posts', CategoryPostView.as_view(), name='category_posts'),
    # path('like-post/<int:pk>/', LikePostView.as_view(), name='like-post'),
]