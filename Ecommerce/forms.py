from .models import *
from django import forms



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["name", "description", "category", "price", "image"]