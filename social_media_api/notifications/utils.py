from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target=None):
    if recipient == actor:
        return

    notif = Notification(recipient=recipient, actor=actor, verb=verb)

    if target is not None:
        notif.target_content_type = ContentType.objects.get_for_model(target.__class__)
        notif.target_object_id = target.pk

    notif.save()
    return notif