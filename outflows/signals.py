from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from outflows.models import Outflow
from services.notify import Notify


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            instance.product.quantity -= instance.quantity
            instance.product.save()


@receiver(post_save, sender=Outflow)
def send_webhook_create_outflow(sender, instance, created, **kwargs):
    notify = Notify()

    data = {
        "event_type": "create_outflow",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "outflow": instance.id,
        "product": instance.product.title,
        "product_selling_price": float(instance.product.selling_price),
        "quantity": instance.quantity,
    }

    notify.send_order_event(data)
