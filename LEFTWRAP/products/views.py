from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.views.decorators.http import require_safe, require_GET, require_POST, require_http_methods
from .models import Product, Sales, Sales_Detail, Category, Comment
from .forms import ProductForm, SalesForm, SalesDetailForm, CategoryForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

@require_safe
def home(request):
    return render(request, 'products/home.html')


@require_safe
def ours(request):
    return render(request, 'products/ours.html')


@require_GET
def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/product_index.html', context)


@require_http_methods(['GET', 'POST'])
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) 
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products:product_detail', product.pk)
    else:
        form = ProductForm()
    context = {
       'form': form,
    }
    return render(request, 'products/product_create.html', context)


@require_safe
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@require_safe
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/product_edit.html', context)


@require_POST
def product_delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
    return redirect('products:product_index')


@login_required
@require_http_methods(["GET", "POST"])
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'movie': product,
    }
    return render(request, 'products:product_update.html', context)


@require_GET
def sale_index(request):
    sales = Sales.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'products/sale_index.html', context)


@require_http_methods(['GET', 'POST'])
def sale_create(request):
    if request.method == 'POST':
        form = SalesForm(request.POST) 
        if form.is_valid():
            sale = form.save(commit=False)
            sale.user = request.user
            sale.save()
            return redirect('products:sale_detail', sale.pk)
    else:
        form = SalesForm()
    context = {
       'form': form,
    }
    return render(request, 'products/sale_create.html', context)


@require_safe
def sale_detail(request, pk):
    sale = get_object_or_404(Sales, pk=pk)
    context = {
        'sale': sale,
    }
    return render(request, 'products/sale_detail.html', context)


@require_safe
def sale_edit(request, pk):
    sale = get_object_or_404(Sales, pk=pk)
    context = {
        'sale': sale,
    }
    return render(request, 'products/sale_edit.html', context)


@require_POST
def sale_delete(request, pk):
    if request.user.is_authenticated:
        sale = get_object_or_404(Sales, pk=pk)
        sale.delete()
    return redirect('products:sale_index')


@login_required
@require_http_methods(["GET", "POST"])
def sale_update(request, pk):
    sale = get_object_or_404(Sales, pk=pk)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('products:sale_detail', sale.pk)
    else:
        form = ProductForm(instance=sale)
    context = {
        'form': form,
        'movie': sale,
    }
    return render(request, 'products:sale_update.html', context)


@require_POST
def sale_like(request, sale_pk):
    if request.user.is_authenticated:
        sale = get_object_or_404(Sales, pk=sale_pk)
        user = request.user

        if sale.like.filter(pk=user.pk).exists():
            sale.like.remove(user)
            like = False
        else:
            sale.like.add(user)
            like = True
        return JsonResponse({'like':like, 'count':sale.like.count()})
    else:
        sale = get_object_or_404(Sales, pk=sale_pk)
        return JsonResponse({'like':False, 'count':sale.like.count()})


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        sale = get_object_or_404(Sales, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.sale = sale
            comment.user = request.user
            comment.save()
        return redirect('products:sale_detail', sale.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, sale_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('products:sale_detail', sale_pk)


@require_GET
def leftwrap(request):
    sales = Sales.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'products/leftwrap_index.html', context)


@require_safe
def leftwrap_edit(request):
    sales = Sales.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'products/leftwrap_edit.html', context)