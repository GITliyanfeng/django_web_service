# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 0003 12:49
# @Author  : __Yanfeng
# @Site    : 
# @File    : signals.py
# @Software: PyCharm
from django.db.models.signals import post_save, pre_save, post_init
from django.dispatch import receiver
from web.models import BlogPost


@receiver(pre_save, sender=BlogPost)
def create_blog_post(sender, instance, **kwargs):
    print('在save之前触发')


@receiver(post_save, sender=BlogPost)
def create_blog_post(sender, instance=None, created=False, update_fields=['markdown'], **kwargs):
    from web.utils.markdown_to_html import markdown
    if created:
        instance.html = markdown(instance.markdown)
        instance.save()

    else:
        print('要触发更新')
        if not instance.current_instance:
            instance.html = markdown(instance.markdown)
            instance.current_instance = True
            instance.save()
