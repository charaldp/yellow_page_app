from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    phone_number = models.CharField(max_length=14, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=50, blank=True)
    comments = models.CharField(max_length=150, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )
