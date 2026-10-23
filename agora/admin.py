from django.contrib import admin

from agora.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "published", "published_at")
    list_filter = ("published",)
    search_fields = ("title", "content")
