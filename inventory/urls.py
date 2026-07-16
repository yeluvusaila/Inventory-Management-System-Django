from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('category/add/', views.add_category, name='add_category'),
    path('category/list/', views.category_list, name='category_list'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),
    path('category/update/<int:id>/',views.update_category,name='update_category'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/list/',views.product_list,name='product_list'),
    path('product/update/<int:id>/',views.update_product,name='update_product'),
    path('product/delete/<int:id>/',views.delete_product,name='delete_product'),
    path('supplier/add/',views.add_supplier,name='add_supplier'),
    path('supplier/list/',views.supplier_list,name='supplier_list'),
    path('supplier/update/<int:id>/',views.update_supplier,name='update_supplier'),
    path('supplier/delete/<int:id>/',views.delete_supplier,name='delete_supplier'),
    path('stock/add/',views.add_stock,name='add_stock'),
    path('stock/list/',views.stock_list,name='stock_list'),
    path('stockout/add/',views.add_stock_out,name='stock_out'),
    path('stockout/list/',views.stockout_list,name='stockout_list'),
]