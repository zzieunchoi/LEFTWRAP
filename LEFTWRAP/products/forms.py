from django import forms
from .models import Product, Sales, Sales_Detail, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','user','image',]


class SalesForm(forms.ModelForm):
    CATE_A = '도넛'
    CATE_B = '페스츄리/파이'
    CATE_C = '조리빵'
    CATE_D = '스낵'
    CATE_E = '베이글'
    CATE_F = '샐러드'
    CATE_G = '케이크'
    CATE_H = '기타'

    CATEGORYS_CHOICES = [
        (CATE_A,'도넛'),
        (CATE_B, '페스츄리/파이'),
        (CATE_C, '조리빵'),
        (CATE_D, '스낵'),
        (CATE_E, '베이글'),
        (CATE_F, '샐러드'),
        (CATE_G, '케이크'),
        (CATE_H, '기타'),
    ]

    category = forms.ChoiceField(
        label='Category',
        choices=CATEGORYS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'my-category form-control',
            }
        )
    )

    class Meta:
        model = Sales
        fields = ['name','price','category','count',]


class SalesDetailForm(forms.ModelForm):
    class Meta:
        model = Sales_Detail
        fields = ['sale','product','count','user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['sale','user']