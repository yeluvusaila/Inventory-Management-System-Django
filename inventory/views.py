from django.shortcuts import render,redirect
from .forms import CategoryForm
from .models import Category
from django.shortcuts import get_object_or_404
from .forms import ProductForm
from .models import Product
from .forms import SupplierForm
from .models import Supplier
from .forms import StockInForm
from .models import StockIn
from django.db.models import Q
from .forms import StockOutForm
from .models import StockOut


def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = CategoryForm()

    return render(request, 'inventory/category_form.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        'inventory/category_list.html',
        {'categories': categories}
    )


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()

    return redirect('/category/list/')

def update_category(request, id):

    category = Category.objects.get(id=id)

    if request.method == 'POST':

        form = CategoryForm(
            request.POST,
            instance=category
        )

        if form.is_valid():
            form.save()

            return redirect('/category/list/')

    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        'inventory/category_form.html',
        {'form': form}
    )

def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/product/list/')

    else:
        form = ProductForm()

    return render(
        request,
        'inventory/product_form.html',
        {'form': form}
    )




def product_list(request):

    q = request.GET.get('q')

    products = Product.objects.all()

    if q:
        products = products.filter(
            product_name__icontains=q
        )

    return render(
        request,
        'inventory/product_list.html',
        {'products': products}
    )

def update_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect('/product/list/')

    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'inventory/product_form.html',
        {'form': form}
    )


def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    return redirect('/product/list/')

def add_supplier(request):

    if request.method == 'POST':

        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/supplier/list/')

    else:
        form = SupplierForm()

    return render(
        request,
        'inventory/supplier_form.html',
        {'form': form}
    )
def supplier_list(request):

    suppliers = Supplier.objects.all()

    return render(
        request,
        'inventory/supplier_list.html',
        {'suppliers': suppliers}
    )

def update_supplier(request, id):

    supplier = Supplier.objects.get(id=id)

    if request.method == 'POST':

        form = SupplierForm(
            request.POST,
            instance=supplier
        )

        if form.is_valid():
            form.save()
            return redirect('/supplier/list/')

    else:
        form = SupplierForm(instance=supplier)

    return render(
        request,
        'inventory/supplier_form.html',
        {'form': form}
    )
def delete_supplier(request, id):

    supplier = Supplier.objects.get(id=id)

    supplier.delete()

    return redirect('/supplier/list/')
def add_stock(request):

    if request.method == 'POST':

        form = StockInForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/stock/list/')

    else:
        form = StockInForm()

    return render(
        request,
        'inventory/stock_form.html',
        {'form': form}
    )
def stock_list(request):

    stocks = StockIn.objects.all()

    return render(
        request,
        'inventory/stock_list.html',
        {'stocks': stocks}
    )
from .models import Category, Product, Supplier, StockIn

def dashboard(request):

    context = {
        'category_count': Category.objects.count(),
        'product_count': Product.objects.count(),
        'supplier_count': Supplier.objects.count(),
        'stock_count': StockIn.objects.count(),
        'stockout_count': StockOut.objects.count(),
        'low_stock_products': Product.objects.filter(quantity__lt=5)
    }

    return render(
        request,
        'inventory/dashboard.html',
        context
    )
def add_stock_out(request):

    if request.method == 'POST':

        form = StockOutForm(request.POST)

        if form.is_valid():

            stock_out = form.save()

            product = stock_out.product

            product.quantity -= stock_out.quantity

            product.save()

            return redirect('/')

    else:
        form = StockOutForm()

    return render(
        request,
        'inventory/stock_out_form.html',
        {'form': form}
    )
def stockout_list(request):

    stockouts = StockOut.objects.all()

    return render(
        request,
        'inventory/stockout_list.html',
        {'stockouts': stockouts}
    )

