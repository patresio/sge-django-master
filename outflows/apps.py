from django.apps import AppConfig


class OutflowsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "outflows"
    verbose_name = "fluxos de saida"

    def ready(self):
        import outflows.signals
