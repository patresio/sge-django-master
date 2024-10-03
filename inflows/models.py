from datetime import datetime

from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify

from products.models import Product
from suppliers.models import Supplier

# Create your models here.


class Inflow(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="inflow",
        verbose_name="fornecedores",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="inflow",
        verbose_name="produtos",
    )
    slug = models.SlugField("slug", null=True, blank=True)
    quantity = models.IntegerField("quantidade")
    description = models.TextField("descrição", blank=True, null=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "fluxo de entrada"
        verbose_name_plural = "fluxos de entrada"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return r("inflows:detail", slug=self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            created_at_new = str(datetime.now())
            created_at_new = (
                created_at_new.replace(":", "")
                .replace("-", "")
                .replace("/", "")
                .replace(" ", "")
            )
            new_slug = str(self.product) + str(self.supplier) + str(created_at_new)
            print(new_slug)
            self.slug = slugify(new_slug)
        return super().save(*args, **kwargs)
