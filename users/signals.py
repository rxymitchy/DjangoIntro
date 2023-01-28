from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
#signals allocate default profile for new users until its updated
@receiver(post_save, sender=User) #receives info of user created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) 

#for saving
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()