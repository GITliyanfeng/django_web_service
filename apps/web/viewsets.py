# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 0005 22:52
# @Author  : __Yanfeng
# @Site    : 
# @File    : viewsets.py
# @Software: PyCharm
from rest_framework import viewsets
from web.models import BlogPost
from web.serializers import BlogpostSerializer
from rest_framework import permissions
from rest_framework.response import Response


class BlogpostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogpostSerializer
    search_fields = 'title'
    queryset = BlogPost.objects.all()

    def list(self, request, *args, **kwargs):
        search_param = self.request.query_params.get('title', None)
        if search_param is not None:
            self.queryset = BlogPost.objects.filter(title__contains=search_param)
        serializer = BlogpostSerializer(self.queryset, many=True)
        return Response(serializer.data)
