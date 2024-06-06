from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name","username","email","id"]

class WaiterAdmin(admin.ModelAdmin):
    list_display = ["user","charge"]

class WaiterShiftAdmin(admin.ModelAdmin):
    list_display = ["waiter","start_date","end_date","restaurant"]


admin.site.register(User,UserAdmin)
admin.site.register(Waiter,WaiterAdmin)
admin.site.register(Waiter_Shift,WaiterShiftAdmin)