from django.db import models



class Person(models.Model):

    RED = 'RD'
    BLUE = 'BL'

    FAV_COLOUR = [
    (RED, 'Red'),
    (BLUE, 'Blue'),
    ]

    class Colours(models.TextChoices):
        RED = 'RD', 'Red'
        BLUE = 'BL', 'Blue'

    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50, choices=Colours.choices)
