from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Category, Book
from django.core.cache import cache
from .tasks import send_book_notification

@receiver(pre_save, sender=Category)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(post_save, sender=Book)        
@receiver(post_delete, sender=Book)
def clear_book_cache(sender, instance, **kwargs):
    cache.clear()
    if kwargs.get('created'):
        send_book_notification.delay(instance.title)
        
    
