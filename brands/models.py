from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify

# Create your models here.


class Brand(models.Model):
    name = models.CharField("nome", max_length=100)
    slug = models.SlugField("slug", blank=True, null=True)
    description = models.TextField("descrição", null=True, blank=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r("brands:detail", slug=self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
