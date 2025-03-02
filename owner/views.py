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
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import logout

@login_required(login_url='userlogin')
def ownerview(request):
    # if not user.is_authenticated:
    #     messages.error(request, 'You are not logged in')
    #     return redirect('userlogin')'
    user = request.user
    if not hasattr(user, 'owner'):
        messages.error(request, 'You are not an owner. We are logging you out.')
        logout(request)
        return redirect('userlogin')
    return render(request, 'owner.html')

@login_required(login_url='userlogin')
def add_product(request):
    user = request.user
    if not hasattr(user, 'owner'):
        messages.error(request, 'You are not an owner. We are logging you out.')
        logout(request)
        return redirect('userlogin')
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
    user = request.user
    if not hasattr(user, 'owner'):
        messages.error(request, 'You are not an owner. We are logging you out.')
        logout(request)
        return redirect('userlogin')
    query_company = request.GET.get("company_name", "")
    query_part = request.GET.get("part_number", "")
    query_car_model = request.GET.get("car_model", "")
    query_description = request.GET.get("description", "")

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


@csrf_exempt
def edit_product(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product_id = data.get('productId')
            product = get_object_or_404(Product, id=product_id)
            product.company_name = data.get('company_name', product.company_name)
            product.part_number = data.get('part_number', product.part_number)
            product.car_model = data.get('car_model', product.car_model)
            product.description = data.get('description', product.description)
            product.mrp = float(data.get('mrp', product.mrp))
            product.discount = float(data.get('discount', product.discount))

            product.save()
            return JsonResponse({"success": True})
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON data"})

    return JsonResponse({"success": False, "error": "Invalid request method"})


@login_required(login_url='userlogin')
def delete_product(request, product_id):
    user = request.user
    if not hasattr(user, 'owner'):
        messages.error(request, 'You are not an owner. We are logging you out.')
        logout(request)
        return redirect('userlogin')
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('search_product')

