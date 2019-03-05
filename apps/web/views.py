from django.shortcuts import render, render_to_response, get_object_or_404
from web.models import BlogPost


# Create your views here.

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {
        'posts': posts
    })


def view_post(request, slug):
    return render(request, 'blogpost_detail.html', {
        'post': get_object_or_404(BlogPost, slug=slug)
    })
