from django.db import  models
from .tender import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product ,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer ,
                                on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)
    phone = models.CharField(max_length=20, default='')
    bidAmt = models.CharField(max_length=50, default='')
    status = models.BooleanField(default=False)
    

    def placeOrder(self):
        self.save()
    
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
              .objects\
              .filter(customer = customer_id)\
              .order_by('-date')
                 
                    