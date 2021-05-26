from datetime import date

from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(verbose_name='Contact Email', null=True, blank=True)
    birthdate = models.DateField(verbose_name='Birthday', null=True, blank=True)
    phone = models.CharField(max_length=10, verbose_name='Phone Number', null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)
    linkedin = models.URLField(verbose_name='LinkedIn Profile Url', null=True, blank=True)
    twitter = models.URLField(verbose_name='Twitter Page Url', null=True, blank=True)
    github = models.URLField(verbose_name='Github', null=True, blank=True)
    resume = models.FileField(verbose_name='Resume', null=True, blank=True, upload_to='resumes/')
    profile_pic = models.ImageField(verbose_name='Profile Picture',
                                    null=True,
                                    upload_to='profile_pics/',
                                    default='default.png')

    def __str__(self):
        return f'{self.name}'

    def age(self):
        if self.birthdate is None:
            return None
        age = relativedelta(date.today(), self.birthdate)
        return age.years


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
