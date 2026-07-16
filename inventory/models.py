from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):

    product_name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.IntegerField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product_name
    
class Supplier(models.Model):

    supplier_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    address = models.TextField()

    def __str__(self):
        return self.supplier_name
class StockIn(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product.product_name
    
class StockOut(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product.product_name