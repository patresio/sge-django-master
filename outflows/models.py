from datetime import datetime

from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify

from products.models import Product


# Create your models here.
class Outflow(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="outflow",
        verbose_name="produtos",
    )
    slug = models.SlugField("slug")
    quantity = models.IntegerField("quantidade")
    description = models.TextField("descrição", blank=True, null=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "fluxo de saida"
        verbose_name_plural = "fluxos de saida"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return r("outflows:detail", slug=self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            created_at_new = str(datetime.now())
            created_at_new = (
                created_at_new.replace(":", "")
                .replace("-", "")
                .replace("/", "")
                .replace(" ", "")
            )
            new_slug = str(self.product) + created_at_new
            self.slug = slugify(new_slug)
        return super().save(*args, **kwargs)
