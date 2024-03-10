from django.db import models

# Create your models here.

class Posts(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(null=True)
