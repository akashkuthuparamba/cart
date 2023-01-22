from django.contrib import admin
from.models import Category,SubCategory,ProductCategory,UserDetails,Item,Cart,Review,PurchaseDetails,ItemQuantite,QuestionAns

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductCategory)
admin.site.register(UserDetails)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(PurchaseDetails)
admin.site.register(ItemQuantite)
admin.site.register(QuestionAns)