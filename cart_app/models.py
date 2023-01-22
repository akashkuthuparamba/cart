from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserDetails(AbstractUser):
    address=models.TextField(blank=True,null=True)
    phone_no=models.IntegerField(blank=True,null=True)
    

class Category(models.Model):
    category_name=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name=models.CharField(max_length=30,blank=True,null=True)
    main_category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_category',blank=True,null=True)

    def __str__(self):
        return self.sub_category_name


class ProductCategory(models.Model):
    product_cate_name=models.CharField(max_length=30,blank=True,null=True)
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='product_category',blank=True,null=True)       

    def __str__(self):
        return self.product_cate_name




class Item(models.Model):
    item_name=models.CharField(max_length=100,blank=True,null=True)
    item_price=models.IntegerField(blank=True,null=True)
    item_img=models.ImageField(upload_to='media/',blank=True,null=True)
    quantitie=models.CharField(max_length=30, blank=True,null=True)
    brand_name=models.CharField(max_length=100, blank=True,null=True)
    quantitie_var=models.CharField(max_length=20,null=True,blank=True)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='item',blank=True,null=True)

    def __str__(self):
        return self.item_name


class Cart(models.Model):
    item_name=models.CharField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='cart',blank=True,null=True) 


class Review(models.Model):
    name=models.CharField(max_length=20, blank=True,null=True)
    message=models.TextField(blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    time=models.TimeField(blank=True,null=True)
    item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='msg',blank=True,null=True)    
     

class PurchaseDetails(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    price=models.CharField(max_length=10,blank=True,null=True)
    quantitie=models.CharField(max_length=30,blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    user=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='details',blank=True,null=True) 


class ItemQuantite(models.Model):
    amount=models.CharField(max_length=20,null=True,blank=True)

class QuestionAns(models.Model):
    question=models.TextField(blank=True,null=True,default=None)
    answer=models.TextField(blank=True,null=True)
    category=models.CharField(max_length=30,blank=True,null=True)
    products=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='question_product',blank=True,null=True)       

   
    def __str__(self):
        return self.question
