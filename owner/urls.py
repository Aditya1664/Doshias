from django.urls import path
from . import views

urlpatterns = [
    path("", views.ownerview, name="owner"),
    path("add/", views.add_product, name="add_product"),
    path("search/", views.search_product, name="search_product"),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    # path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit_product/', views.edit_product, name='edit_product'),
]