# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 0005 22:49
# @Author  : __Yanfeng
# @Site    : 
# @File    : restapi.py
# @Software: PyCharm
from django.contrib.auth.models import User
from rest_framework import serializers
from web.models import BlogPost


class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('title', 'author', 'markdown', 'html', 'slug')
