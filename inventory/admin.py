from django.contrib import admin
from .models import Category,Product,Supplier,StockIn,StockOut

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(StockIn)
admin.site.register(StockOut)