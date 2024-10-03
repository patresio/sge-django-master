from django.contrib import admin

from products.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "brand",
        "category",
        "serial_number",
        "cost_price",
        "selling_price",
        "quantity",
    ]
    search_fields = ["title", "category__name", "brand__name", "serial_number"]


admin.site.register(Product, ProductAdmin)
