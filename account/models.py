from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16, blank=True)
    alt_phone_number = models.CharField(max_length=16, blank=True)
    secondary_email = models.CharField(max_length=50, blank=True)
    profile_photo = models.ImageField(upload_to=user_directory_path)
    skills = models.TextField(blank=True, null=True, max_length=2000)
    specialities = models.TextField(blank=True, null=True, max_length=2000)
    professional_field = models.TextField(blank=True, null=True, max_length=200)
    account_activated = models.BooleanField(default=False)
    date_of_account_activation = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True, max_length=10000)
    age = models.CharField(max_length=3)
    gender = models.TextField(blank=True, null=True, max_length=20)
    time_zone = models.TextField(blank=True, null=True, max_length=200)
    personal_website = models.TextField(blank=True, null=True, max_length=200)
    github = models.TextField(blank=True, null=True, max_length=200)
    instagram = models.TextField(blank=True, null=True, max_length=200)
    twitter = models.TextField(blank=True, null=True, max_length=200)
    facebook = models.TextField(blank=True, null=True, max_length=200)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            instance.userprofile.save()

        post_save.connect(UserProfile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        UserProfile.objects.get_or_create(user=instance)
        instance.userprofile.save()

    def __str__(self):
        return self.user.email

    def set_bio(self, bio):
        self.bio = bio
        return self.bio

    def set_timezone(self, time_zone):
        self.time_zone = time_zone
        return self.time_zone



