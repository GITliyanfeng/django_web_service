from django.db import models


# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    add_time = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return 'title: {}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return 'view_blog_post', None, {'slug': self.slug}
