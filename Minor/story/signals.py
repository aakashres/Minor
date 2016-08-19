from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Story, Response, Rating, Data


@receiver(pre_save, sender=Story)
def create_slug(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug

@receiver(post_save, sender=Response)
def create_rating(sender, instance, *args, **kwargs):
    if instance.is_parent:
        rating = Rating.objects.filter(author=instance.commenter).filter(story= instance.story).first()
        if not rating :
            Rating.objects.create(author=instance.commenter,story= instance.story,rating =instance.rating)
        else:
            rating.rating = instance.rating
            rating.save()