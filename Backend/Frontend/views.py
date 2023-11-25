from django.shortcuts import render
from django.views import View
from . models import Product

# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request,"about_us.html")
class category(View):
    def get(self,request,value):
        products=Product.objects.filter(category=value)
        
           
        return render(request,"category.html",locals())

 