from django.contrib import admin
from . models import Product,Cart,Order



# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=["id","Title","discounted_price","category","prodimg"]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=["product","quantity"]

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=["product","quantity","total"]