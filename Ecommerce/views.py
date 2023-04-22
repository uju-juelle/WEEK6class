from django.shortcuts import render
from .models import *
from .forms import ProductForm
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)# collecting the data
        if form.is_valid(): #validating the data
            form.save()# saving the data
            return HttpResponse("Product has been saved successfully")
        else:
            form = ProductForm()

    products = Product.objects.all()
    form = ProductForm
    context = {
        "list_products": products,
        "form": form
    }
    return render(request, "Ecommerce/home.html", context)


def product_detail_page(request,pk):
    product2 = Product.objects.get(id=pk)
    context = {
        "product": product2
    }
    return render(request, "Ecommerce/detail.html", context)