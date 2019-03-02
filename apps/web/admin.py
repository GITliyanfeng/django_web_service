from django.contrib import admin
from web.models import BlogPost
from django.db import models
from markdown.widgets import AdminMarkdownWidget


# Register your models here.

class BlogPostAdimin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownWidget()},
    }
    exclude = ['add_time']
    prepopulated_fields = {'slug': ('title', 'author')}


admin.site.register(BlogPost, BlogPostAdimin)
