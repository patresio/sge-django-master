from django.contrib import admin

from inflows.models import Inflow

# Register your models here.


class InflowAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "supplier", "quantity", "created_at"]
    search_fields = ["product__title", "supplier__name"]


admin.site.register(Inflow, InflowAdmin)
