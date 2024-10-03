from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify

from brands.models import Brand
from categories.models import Category


# Create your models here.
class Product(models.Model):
    title = models.CharField("titulo", max_length=255)
    slug = models.SlugField("slug", max_length=20)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="categoria",
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name="products", verbose_name="marca"
    )
    description = models.TextField("descricao", blank=True, null=True)
    serial_number = models.CharField(
        "numero de serie", max_length=100, blank=True, null=True
    )
    cost_price = models.DecimalField("preço de custo", max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(
        "preço de venda", max_digits=20, decimal_places=2
    )
    quantity = models.IntegerField("quantidade", default=0)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"
        ordering = ["title"]

    def get_absolute_url(self):
        return r("products:detail", slug=self.slug)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
