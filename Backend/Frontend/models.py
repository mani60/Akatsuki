from django.db import models

CATEGORY_CHOICES=(
    ("toys","toys"),
    ("manga","manga"),
    ("costumes","costumes"),
    ("posters","posters")
)

# Create your models here.\
class Product(models.Model):
    Title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    Description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    prodimg=models.ImageField(upload_to='product')
    quantity=models.PositiveIntegerField(default=0)
    def __str__(self) :
        return self.Title


class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    @property
    def totalcost(self):
        return self.quantity*self.product.discounted_price

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total=models.FloatField()
    @property
    def totalcost(self):
        return self.quantity*self.product.discounted_price






