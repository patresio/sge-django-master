from django.contrib import admin

from outflows.models import Outflow


# Register your models here.
class OutflowAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "quantity", "created_at"]
    search_fields = ["product__title"]


admin.site.register(Outflow, OutflowAdmin)
