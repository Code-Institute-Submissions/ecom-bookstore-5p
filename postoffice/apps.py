from django.apps import AppConfig


class PostofficeConfig(AppConfig):
    name = 'postoffice'

    def ready(self):
        import postoffice.signals