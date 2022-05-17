from django.contrib import admin
from .models import Category, Product, Sales, Sales_Detail, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sales)
admin.site.register(Sales_Detail)
admin.site.register(Comment)