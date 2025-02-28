from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_product, name="add_product"),
    path("add/", views.add_product, name="add_product"),
    path("search/", views.search_product, name="product_list"),
]
