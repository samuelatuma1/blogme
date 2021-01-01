from django.contrib import admin

# Register your models here.
from .models import Post, Comment

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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['post', 'name', 'email', 'active', 'created']
  list_filter = ['active', 'created', 'updated']
  search_fields = ['name', 'email', 'body']

  #Raw id field must be a foreign or many to many field
  raw_id_fields = ['post']

