from django.db import models
from django.shortcuts import resolve_url as r
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField("nome", max_length=100)
    slug = models.SlugField("slug")
    description = models.TextField("descricão", null=True, blank=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r("categories:detail", slug=self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
