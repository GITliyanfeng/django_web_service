from django.db import models


# Create your models here.


class BlogPost(models.Model):
    current_instance = False
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True)
    markdown = models.TextField()
    html = models.TextField()
    add_time = models.DateTimeField(db_index=True, auto_now_add=True)
    update_time = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return 'title: {}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return 'view_blog_post', None, {'slug': self.slug}
