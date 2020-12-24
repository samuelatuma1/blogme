from django.contrib import admin

# Register your models here.
from .models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author' ]
    search_fields = ['title', 'body']
    raw_id_fields = ['author']
    prepopulated_fields = {
                            'slug': ['title']
                          }
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']