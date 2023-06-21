from django.db.models.signals import pre_save
from django.dispatch import  receiver
from os import remove

from ..models import Profile


@receiver(pre_save, sender=Profile)
def pre_save_handler(sender, instance, **kwargs):
    if instance.avatar:
        old_image_uid = instance.user_id
        old_image = sender.objects.get(user_id=old_image_uid)
        if old_image.avatar and not old_image.avatar.path == instance.avatar.path:
            old_image_path = old_image.avatar.path
            remove(old_image_path)
