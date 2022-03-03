from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from Trader.models import Trader


def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='trader')
        instance.groups.add(group)
        Trader.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created!')


post_save.connect(user_profile, sender=User)
