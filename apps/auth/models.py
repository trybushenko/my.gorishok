from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Session(models.Model):
    User = get_user_model()
    user = models.ForeignKey()

