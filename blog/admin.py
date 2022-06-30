from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('title', 'body')
    date_hierarchy = 'date_added'
    ordering = ('date_added',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('body',)



