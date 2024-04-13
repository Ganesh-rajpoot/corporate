from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=128)
    referral_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)
