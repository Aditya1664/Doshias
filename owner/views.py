from django.shortcuts import render, redirect, get_object_or_404
from django.core.files import File
from django.http import HttpResponse
from django.conf import settings
from authentication.models import Owner
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from authentication.models import Product
from .forms import ProductForm

@login_required(login_url='userlogin')
def ownerview(request):
    return render(request, 'owner.html')

@login_required(login_url='userlogin')
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_product')
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})

@login_required(login_url='userlogin')
def search_product(request):
    query_company = request.GET.get("company_name", "")
    query_part = request.GET.get("part_number", "")
    query_car_model = request.GET.get("car_model", "")
    query_description = request.GET.get("description", "")

    # Filtering based on multiple fields
    products = Product.objects.all()
    
    if query_company:
        products = products.filter(company_name__icontains=query_company)
    if query_part:
        products = products.filter(part_number__icontains=query_part)
    if query_car_model:
        products = products.filter(car_model__icontains=query_car_model)
    if query_description:
        products = products.filter(description__icontains=query_description)

    return render(request, "search_product.html", {
        "products": products,
        "query_company": query_company,
        "query_part": query_part,
        "query_car_model": query_car_model,
        "query_description": query_description,
    })
