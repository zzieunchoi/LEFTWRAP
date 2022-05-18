from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('ours/', views.ours, name='ours'),
    path('create/', views.product_create, name='product_create'),
    path('index/', views.product_index, name='product_index'),
    path('detail/', views.product_detail, name='product_detail'),
    path('<int:product_pk>/edit/', views.product_edit, name='product_edit'),
    path('<int:product_pk>/delete/', views.product_delete, name='product_delete'),
    path('<int:product_pk>/update/', views.product_update, name='product_update'),

    path('sales/create/', views.sale_create, name='sale_create'),
    path('sales/index/', views.sale_index, name='sale_index'),
    path('sales/detail/', views.sale_detail, name='sale_detail'),
    path('sales/<int:sale_pk>/edit/', views.sale_edit, name='sale_create'),
    path('sales/<int:sale>/delete/', views.sale_delete, name='sale_delete'),
    path('sales/<int:sale>/update/', views.sale_update, name='sale_update'),
    path('sales/<int:sale>/like', views.sale_like, name='sales_like'),

    path('sales/<int:sale_pk>/comments/create/', views.comments_create, name='comments_create'),
    path('sales/<int:sale_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),

    path('leftwrap/', views.leftwrap, name='leftwrap'),
    path('leftwrap/edit/', views.leftwrap_edit, name='leftwrap_edit'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)