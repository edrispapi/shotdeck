from django.contrib.auth.models import AbstractUser
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    teams = models.ManyToManyField(Team, related_name='members', blank=True)
    # فیلدهای اضافه مثل نقش (role) یا دسترسی می‌توانید اینجا اضافه کنید

    def __str__(self):
        return self.username
