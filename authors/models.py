from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)