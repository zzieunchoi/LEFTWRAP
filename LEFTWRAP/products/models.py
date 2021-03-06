from django.db import models
from django.conf import settings

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Sales(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=30)
    count = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_products')
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    leftwrap = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name


class Sales_Detail(models.Model):
    count = models.IntegerField()
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    content = models.TextField()
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content