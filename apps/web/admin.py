from django.contrib import admin
from web.models import BlogPost
from django.db import models
from markdown.widgets import AdminMarkdownWidget


# Register your models here.

class BlogPostAdimin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownWidget()},
    }
    exclude = ['add_time', 'html']
    prepopulated_fields = {'slug': ('title', 'author')}
    list_display = ('title', 'author', 'slug', 'add_time', 'update_time')


admin.site.register(BlogPost, BlogPostAdimin)
