from django import forms
from .models import Category, Product, Sales, Sales_Detail, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','user','image',]


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['name','price','categorys','count','like']


class SalesDetailForm(forms.ModelForm):
    class Meta:
        model = Sales_Detail
        fields = ['sale','product','count','user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['sale','user']