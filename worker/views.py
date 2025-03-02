from django.shortcuts import render, redirect, get_object_or_404
from django.core.files import File
from django.http import HttpResponse
from django.conf import settings
from authentication.models import Worker
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from .forms import ProductForm
from authentication.models import Product
from django.contrib import messages
from django.contrib.auth import logout

@login_required(login_url='userlogin')
def worker(request):
    
    # if not user.is_authenticated:
    #     messages.error(request, 'You are not logged in')
    #     return redirect('userlogin')
    user = request.user
    if not hasattr(user, 'worker'):
        messages.error(request, 'You are not a worker. We are logging you out.')
        logout(request)
        return redirect('userlogin')
    return render(request, 'worker.html')

@login_required(login_url='userlogin')
def search_product(request):
    user = request.user
    if not hasattr(user, 'worker'):
        messages.error(request, 'You are not a worker. We are logging you out.')
        logout(request)
        return redirect('userlogin')
    
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

    return render(request, "find_product.html", {
        "products": products,
        "query_company": query_company,
        "query_part": query_part,
        "query_car_model": query_car_model,
        "query_description": query_description,
    })
