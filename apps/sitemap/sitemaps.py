# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 0005 20:48
# @Author  : __Yanfeng
# @Site    : 
# @File    : sitemaps.py
# @Software: PyCharm
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from django.apps import apps as django_apps
from web.models import BlogPost


class PageSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['main']

    def location(self, obj):
        return reverse(obj)


class FlatPageSitemap(Sitemap):
    priority = 0.8

    def items(self):
        Site = django_apps.get_model('sites.Site')
        current_site = Site.objects.get_current()
        return current_site.flatpage_set.filter(registration_required=False)


class BlogSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.add_time
