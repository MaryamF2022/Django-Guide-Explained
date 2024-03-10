from typing import Collection, Optional
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os
from django.db.models import F
from django.core.exceptions import ValidationError
from django.db.models import F
from django.db.models.functions import Lower
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Product Name', max_length=10)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'Product: {self.name}'
    

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


import datetime
import unittest

class MoonLanding(datetime.date, models.Choices):
    APOLLO_11 = 1969, 7, 20, 'Apollo 11 (Eagle)'
    APOLLO_12 = 1969, 11, 19, 'Apollo 12 (Intrepid)'
    APOLLO_14 = 1971, 2, 5, 'Apollo 14 (Antares)'
    APOLLO_15 = 1971, 7, 30, 'Apollo 15 (Falcon)'
    APOLLO_16 = 1972, 4, 21, 'Apollo 16 (Orion)'
    APOLLO_17 = 1972, 12, 11, 'Apollo 17 (Challenger)'


class Moon(models.Model):
    moon_landing = models.DateField(
        choices = MoonLanding.choices,
        default = MoonLanding.APOLLO_11,
        db_column='landing_date'
    )


def user_directory_path(instance, filename):
    # username = instance.user.username
    # timestamp = timezone.now().strftime('%Y/%m/%d')
    # filename = f'{username}_{timestamp}_{filename}'

    return 'inventory/uploads/user_{0}/{1}'.format(instance.user.id, filename)

class NewFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=user_directory_path)

class MyModel(models.Model):
    val = models.IntegerField()

    def clean_fields(self, exclude):
        if self.val >= 20:
            raise ValidationError(f"values musn't be bigger than 20")
        return super().clean_fields(exclude)
    
    def save(self):
        self.clean_fields(exclude=None)
        return super().save()

class Test(unittest.TestCase):

    def test_update_result(self):
        obj = MyModel.objects.create(val=1)
        MyModel.objects.filter(pk=obj.pk).update(val = F('val') + 1)
        obj.refresh_from_db()
        self.assertEqual(obj.val, 2)


class Singer(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField('Band', related_name='Membership', through='Member')


class Band(models.Model):
    name = models.CharField(max_length=100)

class Member(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)


class Symmetric(models.Model):
    follower = models.ManyToManyField('self', symmetrical=True)

class AsSymmetric(models.Model):
    follower = models.ManyToManyField('self', symmetrical=False)

class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(my_field="A")

class MyTest(models.Model):
    my_field = models.CharField(max_length=200)
    manager = BookManager()
    objects = models.Manager()

    class Meta:
        base_manager_name= 'objects'
        default_manager_name='manager'

class Question(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField()
    when = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['when','name']

class Answers(models.Model):
    name= models.CharField(max_length=100)
    quest = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer= models.TextField()

    # class Meta:
    #      order_with_respect_to = 'quest'

class BookPages(models.Model):
    page_num = models.IntegerField()
    content = models.TextField()

    class Meta:
        indexes = [models.Index((F('page_num')**2).desc(), name='mul_page_num'),
                   models.Index(fields=['content'], include=['page_num'], name='inc_page_num'),
                   models.Index(F('content').asc(), name='lower_content')]
        
class UniqueModel(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint('field1',Lower('field2').desc(), name='unique_fields_constraint')
        ]


class Client(models.Model):
    REGULAR = 'R'
    GOLD ='G'
    PLATINUM= 'P'

    ACCOUNT_TYPE_CHOICES = [
        (REGULAR, "Regular"),
        (GOLD, "Gold"),
        (PLATINUM, "Platinum"),
    ]

    name = models.CharField(max_length=50)
    registered_on = models.DateField()
    account_type = models.CharField(
        max_length=1,
        choices = ACCOUNT_TYPE_CHOICES,
        default = REGULAR
    )

class AbsBase(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        abstract = True
        db_table = 'inventory_band'


class AbsChild(models.Model):
    age= models.IntegerField()

    class Meta:
        pass
    
class Place(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=['content_type', 'object_id'])
        ]
    
class Bookmark(models.Model):
    url = models.URLField()
    tags = GenericRelation(TaggedItem, related_query_name='bookmark')

class ProductNew(models.Model):
    name = models.CharField(max_length=102)

class Review(models.Model):
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    product = models.ForeignKey(ProductNew, related_name='review', on_delete=models.CASCADE)




class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='entry')
    headline = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    

    def __str__(self):
        return self.headline