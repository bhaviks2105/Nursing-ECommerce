from django.db import models
from django.contrib.auth.models import User


# Create your 0models here.
category_choice=(
    ('in','indoorplants'),
    ('fl','flowering'),
    ('se','season'),
    ('fe','foliage'),
)

STATUS_CHOICE=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),

)

class Product(models.Model):
    title = models. CharField(max_length=100)
    selling_price = models. FloatField()
    discounted_price = models. FloatField()
    description = models. TextField()
    category = models. CharField(choices=category_choice, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Customer(models.Model):
     user = models. ForeignKey(User, on_delete=models.CASCADE)
     name = models. CharField (max_length=200)
     locality = models. CharField (max_length=200)
     city =models.CharField (max_length=50)
     mobile=models.IntegerField (default=0)
     zipcode = models.IntegerField()
     state = models.CharField(max_length=100)

     def _str_(self):
        return self.name

class Cart(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)

     @property
     def total_cost(self):
        return self.quantity * self.product.discounted_price



class Payment(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       amount = models.FloatField()
       razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
       razorpay_payment_status = models.CharField(max_length=100,blank=True, null=True)
       razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
       paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
       product = models.ForeignKey(Product, on_delete=models.CASCADE)
       quantity = models.PositiveIntegerField (default=1)
       ordered_date = models.DateTimeField (auto_now_add=True)
       status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Pending')
       payment = models.ForeignKey(Payment, on_delete=models. CASCADE, default="")

       @property
       def total_cost(self):
        return self.quantity * self.product.discounted_price





class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
