from django.db import models

from fontawesome_5.fields import IconField

class Category(models.Model):
    
    icon = IconField()
# Create your models here.
