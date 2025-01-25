from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.posts_list, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="blog-posts"),
]
