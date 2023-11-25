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
    def __str__(self) :
        return self.Title




