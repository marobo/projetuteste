from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_on')
    list_filter = ('id', 'title',)
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
