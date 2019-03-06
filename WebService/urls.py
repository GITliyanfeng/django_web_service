"""WebService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.contrib import admin
from web import views as web_views
from django.contrib.sitemaps.views import sitemap
from sitemap.sitemaps import PageSitemap, FlatPageSitemap, BlogSitemap

from rest_framework import routers
from web.viewsets import BlogpostViewSet

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost', BlogpostViewSet, basename='Blogpost')

sitemaps = {
    'Page': PageSitemap,
    'Flatpages': FlatPageSitemap,
    'Blog': BlogSitemap
}

urlpatterns = [
    url(r'^$', web_views.index, name='main'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/(?P<slug>[^.]+).html', web_views.view_post, name='view_blog_post'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api/', include(apiRouter.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='res_framework')),
]
