from django.apps import AppConfig


class BrandsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "brands"
    verbose_name = "marcas"

    def ready(self):
        import brands.signals
