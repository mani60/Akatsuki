from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Cart
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
default = 5
min_val = 1
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about_us.html")

class category(View):
    def get(self,request,value):
        products=Product.objects.filter(category = value)
        return render(request,"category.html",locals())

class productDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk = pk)
        p_cat = product.category
        R_prods = Product.objects.filter(category= p_cat).exclude(pk=pk)
        return render(request,"product_details.html",locals())

def add_to_cart(request):
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(product=product).save()
    product.quantity-=1
    product.save()
    return redirect("/cart")

def cart(request):
    cart = Cart.objects.all()
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    amount = round(amount, 2)
    total_amount = round(amount + 40,2)
    return render(request,"cart.html",locals())

def custom_404(request, exception):
    return render(request, '404.html')

def IncCart(request):
    if request.method == "GET":
        prod_id =  request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        c = Cart.objects.get(product=product)
        if product.quantity <= default and c.quantity < default:
            product.quantity-=1
            c.quantity+=1
            c.save()
            product.save()
        else:
            pass
        cart = Cart.objects.all()
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        amount = round(amount, 2)
        total_amount = round(amount + 40,2)
        data={
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)
def DecCart(request):
    if request.method == "GET":
        prod_id =  request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        c = Cart.objects.get(product=product)
        if product.quantity >= 0 and c.quantity>min_val:
            c.quantity-=1
            product.quantity+=1
            product.save()
            c.save()
        cart = cart = Cart.objects.all()
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        amount = round(amount, 2)
        total_amount = round(amount + 40,2)
        data={
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)

def RemoveItem(request):
    if request.method == "GET":
        prod_id =  request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        c = Cart.objects.get(product=product)
        product.quantity+=c.quantity
        product.save()
        c.delete()
        cart = cart = Cart.objects.all()
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        amount = round(amount, 2)
        total_amount = round(amount + 40,2)
        data={
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)