from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


all_posts = Post.objects.all().order_by("-title")


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": all_posts})


def posts_list(request):
    return render(request, "blog/posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(
        request, "blog/post-detail.html", {"post": post, "tags": post.tag.all()}
    )
