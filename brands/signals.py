from django.db.models.signals import pre_save
from django.dispatch import receiver

from brands.models import Brand
from services.gemini import get_brand_description


@receiver(pre_save, sender=Brand)
def pre_save_brand_ia_description(sender, instance, **kwargs):
    if not instance.description:
        ai_description = get_brand_description(instance.name)
        instance.description = ai_description
