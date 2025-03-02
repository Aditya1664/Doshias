from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker, name='worker'),
    path("search/", views.search_product, name="find_product"),
    ]