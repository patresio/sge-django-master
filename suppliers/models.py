from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify

from suppliers.managers import KindQuerySet


# Create your models here.
class Supplier(models.Model):
    name = models.CharField("nome", max_length=100)
    slug = models.SlugField("Slug")
    description = models.TextField("descrição", null=True, blank=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "fornecedor"
        verbose_name_plural = "fornecedors"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r("suppliers:detail", slug=self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Contact(models.Model):
    EMAIL = "E"
    PHONE = "P"
    KINDS = ((EMAIL, "Email"), (PHONE, "Phone"))
    suppliers = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, verbose_name="fornecedores"
    )
    kind = models.CharField("tipo", max_length=1, choices=KINDS)
    value = models.CharField("valor", max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = "contato"
        verbose_name_plural = "contatos"

    def __str__(self):
        return self.value
