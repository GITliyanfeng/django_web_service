# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 0005 22:52
# @Author  : __Yanfeng
# @Site    : 
# @File    : viewsets.py
# @Software: PyCharm
from rest_framework import viewsets
from web.models import BlogPost
from web.serializers import BlogpostSerializer


class BlogpostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer
