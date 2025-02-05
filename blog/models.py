from django.db import models
from django.urls import reverse
from django.core.validators import (
    MinLengthValidator,
)


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "tag"


class Author(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Users"


class Post(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    content = models.TextField(validators=[MinLengthValidator(5)])
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(max_length=100, unique=True)
    tag = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("blog-posts", args=[self.slug])

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return f"Comment By {self.user_name}"
     