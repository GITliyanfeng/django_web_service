from django.apps import AppConfig


class WebConfig(AppConfig):
    name = 'web'
    verbose_name = '文章'

    def ready(self):
        import web.signals
