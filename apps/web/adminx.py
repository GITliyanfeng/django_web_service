# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 0003 17:20
# @Author  : __Yanfeng
# @Site    : 
# @File    : xadmin.py
# @Software: PyCharm
import xadmin
from xadmin import views
from web.models import BlogPost
from markdown.widgets import XAdminMarkdownWidget
from django.db import models


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '我的后台管理'
    site_footer = '@我的后台xadmin'


class BlogPostAdmin(object):
    list_display = [
        'title',
        'author',
        'slug',
        'add_time',
        'update_time'
    ]
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }
    search_fields = ['title', 'author']
    # list_editable = ['author']
    list_filter = ['title', 'author']
    exclude = ['add_time', 'html']


# xadmin.site.register(BlogPost, BlogPostAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSetting)
