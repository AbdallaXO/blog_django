from django.contrib import admin

# Register your models here.
from .models import Tag, Author, Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tag")
    list_display = (
        "title",
        "date",
        "author",
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "author")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post", "time", "date")
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
