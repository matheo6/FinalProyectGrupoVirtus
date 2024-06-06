from django.contrib import admin
from .models import *
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name","address","owner"]
class ProductRestaurantAdmin(admin.ModelAdmin):
    list_display = ["product","restaurant"]
class TableAdmin(admin.ModelAdmin):
    list_display = ["id","number","personCapacity"]
class TablesrestaurantAdmin(admin.ModelAdmin):
    list_display = ["table","restaurant"]

class OrdersAdmin(admin.ModelAdmin):
    list_display = ["waiter","tableRestaruant"]
class ProductsOrderAdmin(admin.ModelAdmin):
    list_display = ["product","order"]
class BillsAdmin(admin.ModelAdmin):
    list_display = ["order","cost"]
class TipWaiterAdmin(admin.ModelAdmin):
    list_display = ["bill","waiter","paid"]

    
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Product_Restaurant,ProductRestaurantAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Tables_restaurant,TablesrestaurantAdmin)
admin.site.register(Order,OrdersAdmin)
admin.site.register(Products_order,ProductsOrderAdmin)
admin.site.register(Bill,BillsAdmin)
admin.site.register(Tip_waiter,TipWaiterAdmin)