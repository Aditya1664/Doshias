from django.urls import path
from . import views

urlpatterns = [
    path("", views.ownerview, name="owner"),
    path("add/", views.add_product, name="add_product"),
    path("search/", views.search_product, name="search_product"),
]