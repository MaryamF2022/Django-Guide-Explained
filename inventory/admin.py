from django.contrib import admin
from .models import Product, Category, Stock, MyModel

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(MyModel)
