from django.contrib import admin
from web.models import BlogPost


# Register your models here.
class BlogPostAdimin(admin.ModelAdmin):
    exclude = ['add_time', 'html']
    prepopulated_fields = {'slug': ('title', 'author')}
    list_display = ('title', 'author', 'slug', 'add_time', 'update_time')


admin.site.register(BlogPost, BlogPostAdimin)
