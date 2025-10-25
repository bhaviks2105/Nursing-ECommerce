from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
# Create your views here.
from django.views import View
from .models import Product,Cart,OrderPlaced,Payment,ContactMessage
from django.contrib import messages
from.froms import CustomerRegistrationForm,CustomerProfileForm,Customer,PasswordChangeForm,MyPasswordResetForm
from django.db.models import Q
from django.shortcuts import redirect
from django.conf import settings
import razorpay
from  django.contrib.auth.decorators import login_required





def home(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"plants/home.html",locals())


def about(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"plants/about.html",locals())

def contact(request):
        if request.method == 'POST':
         contact = ContactMessage()
         name = request.POST.get('name')
         email = request.POST.get('email')
         message = request.POST.get('message')
         contact.name = name
         contact.email = email
         contact.message = message
         contact.save()
         messages.success(request,"GO Green  and Thanks!")
         totalitem = 0
         if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'plants/contact.html',locals())


class CategoryView(View):
     def get (self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "plants/category.html", locals())


class CategoryTitle(View):
    def get (self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "plants/category.html", locals())


class ProductDetail(View):
    def get (self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "plants/productdetail.html" , locals())


class CustomerRegistrationView(View):
    def get(self,request):
      form = CustomerRegistrationForm()
      return render(request, "plants/customerregistration.html", locals())
    def post(self,request):
      form = CustomerRegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request,"GO Green !")
      else:
        messages.warning(request,"Invalid")

      totalitem = 0
      if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
      return render(request, "plants/customerregistration.html", locals())




class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, "plants/profile.html" , locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)

        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")

        else:
          messages.warning(request, "Invalid Input Data")

        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "plants/profile.html" , locals())


def address(request):
     add = Customer.objects.filter(user=request.user)
     totalitem = 0
     if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'plants/address.html',locals())

class UpdateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form= CustomerProfileForm(instance=add)
        return render(request,'plants/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.user = request.user
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile Save Successfully")

        else:
          messages.warning(request, "Invalid Input Data")

        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return redirect("address")


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()

    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return redirect("/cart")

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount= 0
    for p in cart:
        value= p.quantity * p.product.discounted_price
        amount= amount + value
    totalamount = amount + 50
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,'plants/addtocart.html',locals())



@method_decorator(login_required,name='dispatch')
class checkout(View):
     def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 50
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = {
            "amount": razoramount,
            "currency": "INR",
            "receipt": "order_rcptid_11",
        }
        payment_response = client.order.create(data=data)
        print(payment_response)
        #{'id': 'order_MXnYIA31k5ZGVP', 'entity': 'order', 'amount': 144000, 'amount_paid': 0, 'amount_due': 144000,'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1693730034}
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status,

            )
            payment.save()
        return render(request,'plants/checkout.html',locals())

@login_required
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    customer = Customer.objects.get(id=cust_id)
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()

    return redirect(orders)
@login_required
def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request,'plants/orders.html',locals())
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.filter(product=prod_id, user=request.user).first()
        if c is not None:
            # The product is already in the cart, so increase the quantity
            c.quantity += 1
            c.save()
        else:
            # The product is not in the cart, so add it
            c = Cart.objects.create(product=prod_id, user=request.user)
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 50
        data = {'quantity': c.quantity, 'amount': amount, 'totalamount': totalamount}
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.filter(product=prod_id, user=request.user).first()
        if c is not None:
            # The product is already in the cart, so decrease the quantity
            if c.quantity > 1:
                c.quantity -= 1
                c.save()
            else:
                # The product quantity is 1, so remove it from the cart
                c.delete()
        else:
            # The product is not in the cart, so do nothing
            pass
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 50
        data = {'quantity': c.quantity, 'amount': amount, 'totalamount': totalamount}
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.filter(product=prod_id, user=request.user).first()
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 50
        data = {'amount': amount, 'totalamount': totalamount}
        return JsonResponse(data)




def search(request):
    query = request.GET.get('search')
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "plants/search.html",{'product':product})





