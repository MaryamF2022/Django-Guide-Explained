from typing import Iterable, Optional
from django.db import models
from django.template.defaultfilters import slugify

class Books(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    count = models.IntegerField(null=True, default=0)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args, **kwargs)
