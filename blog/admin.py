from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['author', 'status', 'publish']
    search_fields = ['author', 'title']
    prepopulated_fields = {"slug" : ['title']}
    list_editable = ['status', 'author']


