from django.contrib import admin

# Register your models here.
from .models import Tag, Author, Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tag")
    list_display = (
        "title",
        "date",
        "author",
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "author")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
