from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page"),
]
