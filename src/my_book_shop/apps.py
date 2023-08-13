from django.apps import AppConfig


class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_book_shop'

    def ready(self):
        import my_book_shop.signals