from django.contrib import admin
from .models import Product
from .models import Owner
from .models import Worker
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("company_name", "part_number", "car_model", "description", "final_price","c_price","m_price")

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("oname", "contact_num","email", "gender")

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("wname", "contact_num","email", "gender")