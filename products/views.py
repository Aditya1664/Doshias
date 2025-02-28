from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, "home")
 
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})

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
