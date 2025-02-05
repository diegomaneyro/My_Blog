from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to=('Profiles'), blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    twitter = models.URLField(max_length=50, blank=True, null=True)
    linkedin = models.URLField(max_length=50, blank=True, null=True)
    facebook = models.URLField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
