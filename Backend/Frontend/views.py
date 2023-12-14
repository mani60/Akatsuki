from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Cart,Order,Wishlist
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
default = 5
min_val = 1
def home(request):
    totalitems=0
    totalitems=len(Cart.objects.all())
    wishitems=0
    wishitems=len(Wishlist.objects.all())
    return render(request, "home.html",locals())

def about(request):
    totalitems=0
    totalitems=len(Cart.objects.all())
    wishitems=0
    wishitems=len(Wishlist.objects.all())
    return render(request,"about_us.html",locals())

class category(View):
    def get(self,request,value):
        totalitems=0
        totalitems=len(Cart.objects.all())
        wishitems=0
        wishitems=len(Wishlist.objects.all())
        products=Product.objects.filter(category = value)
        return render(request,"category.html",locals())

class productDetail(View):
    def get(self,request,pk):
        totalitems=0
        totalitems=len(Cart.objects.all())
        wishitems=0
        wishitems=len(Wishlist.objects.all())
        product = Product.objects.get(pk = pk)
        wishlist=Wishlist.objects.filter(product=product).exists()
        p_cat = product.category
        R_prods = Product.objects.filter(category= p_cat).exclude(pk=pk)
        return render(request,"product_details.html",locals())

def add_to_cart(request):
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    c=Cart.objects.filter(product=product).exists()
    if c:
        add = Cart.objects.get(product=product)
        add.quantity+=1
        add.save()
    else:
        Cart(product=product).save()
    product.quantity-=1
    product.save()
    return redirect("/cart")

def cart(request):
    totalitems=0
    totalitems=len(Cart.objects.all())
    wishitems=0
    wishitems=len(Wishlist.objects.all())
    cart = Cart.objects.all()
    amount = 0
    for p in cart:
        value = p.quantity * p.product.selling_price
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
            value = p.quantity * p.product.selling_price
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
            value = p.quantity * p.product.selling_price
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
        cart = Cart.objects.all()
        amount = 0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        amount = round(amount, 2)
        total_amount = round(amount + 40,2)
        data={
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)


def add_to_Order(request):
    total=request.GET.get('total_amt')
    cart = Cart.objects.all()
    for data in cart:
        total = data.quantity * data.product.selling_price
        Order(
            product=data.product, 
            quantity=data.quantity,
            total = total
        ).save()
    cart.delete() 
    return redirect("/Orders")

def Orders(request):
    totalitems=0
    totalitems=len(Cart.objects.all())
    wishitems=0
    wishitems=len(Wishlist.objects.all())
    Orders = Order.objects.all()
    amount = 0
    for p in Orders:
        amount += p.total 
    amount = round(amount, 2)
    total_amount = round(amount + 40,2)
    return render(request,"Orders.html",locals())


def search(request):
    totalitems=0
    totalitems=len(Cart.objects.all())
    wishitems=0
    wishitems=len(Wishlist.objects.all())
    query=request.GET["search_product"]
    products=Product.objects.filter(Title__icontains=query)
    return render(request,"search.html",locals())


def Incwish(request):
    if request.method == "GET":
        prod_id =  request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        Wishlist(product=product).save()
       
        data={
            'message':'added to wishlist successfully'
            
        }
        return JsonResponse(data)

def Decwish(request):
    if request.method == "GET":
        prod_id =  request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        Wishlist.objects.filter(product=product).delete()
       
        data={
            'message':'removed from wishlist'
            
        }
        return JsonResponse(data)
    

def wishList(request):
    totalitems=0
    totalitems=len(Cart.objects.all())
    wishitems=0
    wishitems=len(Wishlist.objects.all())
    products = Wishlist.objects.all()
    return render(request,"wishlist.html",locals())


