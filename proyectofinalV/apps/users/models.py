from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    first_name=models.CharField(max_length=60,null=False,blank=False)

    REQUIRED_FIELDS = ["first_name","email"]
    
    def save(self, *args,**kwargs) -> None:
        self.username=self.email.split("@")[0]
        return super().save( *args,**kwargs)
       
class Waiter(models.Model):
    options_charge = [ 
            ('MG', 'MANAGER'),
            ('AT', 'ADMINTABLES'), 
            ('EX', 'EXTRA') 
            ]
    user= models.ForeignKey(User,on_delete=models.DO_NOTHING)
    charge=models.CharField(max_length=20,null=False,blank=False,choices=options_charge,default='EX')

class Waiter_Shift(models.Model):
    waiter= models.ForeignKey(Waiter,on_delete=models.DO_NOTHING)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    restaurant=models.ForeignKey('restaurant.Restaurant', on_delete=models.DO_NOTHING)
     