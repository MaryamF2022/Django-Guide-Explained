from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Book(models.Model):
    class BookStatus(models.TextChoices):
        PUBLISHED = 'pub', 'published'
        UNPUBLISHED = 'unpub', 'unpublished'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=5,choices=BookStatus.choices, default=BookStatus.PUBLISHED)
    date_published = models.DateField(null=True, blank=True)
    commentors = models.ManyToManyField('Commentors', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    @admin.display(description='Commentors', ordering='-title')
    def author_list(self):
        return ', '.join([commentor.name for commentor in self.commentors.all()])
    
    @admin.display
    def colored_color_details(self):
        return format_html(
            "<span style='color: {};'>{} {}</span>",
            'red',
            self.title,
            self.author
        )

class Commentors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()

    def __str__(self) -> str:
        return self.name


    

