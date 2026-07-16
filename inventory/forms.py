from django import forms
from .models import Category,Product,Supplier
from .models import StockIn,StockOut

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'product_name',
            'price',
            'quantity',
            'category']
    
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'}),
        }
class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier

        fields = [
            'supplier_name',
            'phone',
            'email',
            'address'
        ]

        widgets = {
            'supplier_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
        }
class StockInForm(forms.ModelForm):

    class Meta:
        model = StockIn
        fields = '__all__'

class StockOutForm(forms.ModelForm):

    class Meta:
        model = StockOut
        fields = '__all__'