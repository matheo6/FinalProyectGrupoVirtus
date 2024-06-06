from django.db import models

#import form other apps
from apps.users.models import *
from apps.products.models import Product
# Create your models here.

class Restaurant(models.Model):
    name= models.CharField(max_length=60,blank=False,null=False)
    address=models.CharField(max_length=60, blank=False,null=False)
    owner= models.ForeignKey(User,on_delete= models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name
    
class Product_Restaurant(models.Model):
    product= models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    restaurant= models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)

class Table(models.Model):
    number= models.IntegerField( blank=False,null=False)
    personCapacity=models.IntegerField(blank=False,null=False)

class Tables_restaurant(models.Model):
    table= models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)

class  Order(models.Model):
    waiter= models.ForeignKey(Waiter,on_delete=models.DO_NOTHING)
    tableRestaruant=models.ForeignKey(Tables_restaurant,on_delete=models.DO_NOTHING)


class Products_order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    order= models.ForeignKey(Order,on_delete=models.DO_NOTHING)

class Bill(models.Model):
    order= models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    cost= models.IntegerField(blank=False,null=False)
    tip_percent=models.DecimalField(max_digits=2,decimal_places=2,default=0.2)
    final_cost=models.FloatField(blank=False,null=False,default=0)


class Tip_waiter(models.Model):
    bill= models.ForeignKey(Bill,on_delete=models.DO_NOTHING)
    waiter= models.ForeignKey(Waiter,on_delete=models.DO_NOTHING)
    paid= models.BooleanField(null=False,blank=False)

