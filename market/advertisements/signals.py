from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ReplyModel

import django.dispatch


reply_is_accepted = django.dispatch.Signal()


@receiver(post_save, sender=ReplyModel)
def notify_advert_user(sender, instance, created, **kwargs):
    if created:
        email = EmailMessage(subject='[MMORPG_MRKT] New reply',
                             body='You got a new reply to your ad. Check your personal account.',
                             to=[instance.advert.user.email])
        email.send()


@receiver(reply_is_accepted)
def notify_reply_user(sender, email, **kwargs):
    email = EmailMessage(subject='[MMORPG_MRKT] Reply is accepted',
                         body='Your reply has been accepted. Do nothing.',
                         to=[email])
    email.send()
