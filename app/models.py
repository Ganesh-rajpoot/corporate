from django.db import models
from django.utils import timezone

'''This model is for Student who registerd with us'''
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

'''This model is for mentor who teach to student'''
class Mentor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_id = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(Mentor, self).save(*args, **kwargs)  

class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name    