from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Cart

# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request,"about_us.html")
class category(View):
    def get(self,request,value):
        products=Product.objects.filter(category=value)
        return render(request,"category.html",locals())

def add_to_cart(request):
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(product=product).save()
    return redirect("/cart")
def cart(request):
    cart=Cart.objects.all()
    return render(request,"cart.html",locals())

 