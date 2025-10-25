from django.contrib import admin
from.models import Product,Customer,Cart,OrderPlaced,Payment,ContactMessage
# Register your models here.

@admin.register(Product)
class ProudctModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['user','locality','city','mobile','zipcode','state']



@admin.register(Cart)
class CaerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','quantity','ordered_date','status','payment']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display =['name','email','message']