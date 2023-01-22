from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Category,Item,SubCategory,Cart,UserDetails,Review,PurchaseDetails,ProductCategory,QuestionAns
import datetime
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def home_view(request):
    cate=Category.objects.all()
    question_ans=QuestionAns.objects.filter(category="general")
    
    if request.method=='POST' and "search" in request.POST:
        search=request.POST['search']
        print(search)
        data=Item.objects.filter(item_name=search)
        return render(request,'item.html',{"item":data})
    

    return render(request,'home.html',{"cate":cate,"question_ans":question_ans,"category":"general"})


def product_question(request,category):
    print(request.POST["product"])
    if "question" in request.POST:   
        question=request.POST["question"]
        # category=request.POST["category"]
    
        product=Item.objects.get(pk=request.POST["product"]) if "product" in request.POST else None
        if  question is not None:   
            QuestionAns.objects.create(question=question,category=category,products=product)
    return redirect('cart_app:home')

 
            

def list(request):
    data=Item.objects.all()
    cate=Category.objects.all()
    return render(request,'list.html',{"data":data, "cate":cate})


def item_view(request,pk):
    data=SubCategory.objects.get(pk=pk)
    return render(request,'item.html',{"data":data})


def cart_view(request,pk):
    user=request.user
    item=Item.objects.get(id=pk)
    item_name=item.item_name
    print(item_name)
    obj=Cart.objects.create(item_name=item_name,user=user)
    obj.save()
    return redirect('cart_app:home')


def detail_view(request,pk):
    data=Item.objects.get(id=pk)
    user=request.user
    question_ans=QuestionAns.objects.filter(category="product",products=pk)
    if request.method=="POST":
        q=data.item_name
        print(type(q))
        item=data
        message=request.POST['review']
        date=datetime.datetime.now().date()
        time=datetime.datetime.now().time()
        user=request.user.username
        details=Review.objects.create(message=message,date=date,time=time,name=user,item=item)
        details.save()
    return render(request,'detail.html',{"data":data,"user":user,"category":"product","question_ans":question_ans})    


def edit_view(request,id):
    data=request.user
    item=Item.objects.get(id=id)
    if request.method=="POST":
        data.first_name=request.POST['first_name']
        data.last_name=request.POST['last_name']
        data.address=request.POST['address']
        data.email=request.POST['email']
        data.phone_no=request.POST['phone_no']
        data.save()
        print(id)
        return redirect('cart_app:edit' , id)
    return render(request,'edit.html',{"user":data,"item":item})    


def buy_view(request,id):
    user=request.user
    details=Item.objects.get(id=id)
    name=details.item_name
    price=details.item_price
    quantitie=details.quantitie
    date=datetime.date.today()
    purchase=PurchaseDetails.objects.create(name=name,price=price,quantitie=quantitie,user=user,date=date)
    purchase.save() 
    return render(request,'success.html',{"user":user})


def logout_view(request):
    logout(request)
    return redirect('cart_app:home')    


def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        myuser=authenticate(username=username,password=password)
        print(myuser)
        if myuser is not None:
            print("logged in")
            login(request,myuser)
            return redirect('cart_app:home')
    return render(request,'login.html')


def register_view(request):
    if request.method=="POST":
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            address=request.POST['address']
            phone_no=request.POST['phone_no']
            myuser=UserDetails.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,address=address,phone_no=phone_no)
            print(myuser)
            myuser.save()
            return redirect('cart_app:login') 
    return render(request,'register.html')    


def account_view(request):
    user=request.user
    return render(request,'account.html',{"user":user})


def order_view(request):
    user=request.user
    return render(request,'order.html',{"user":user})


def cart_detail_view(request):
    user=request.user
    obj=[]
    val=0
    data=user.cart.all()
    for item in data:
        x=Item.objects.filter(item_name=item.item_name)
        obj+=x
        for price in x:
            val+=price.item_price
    print(val)          
    return render(request,'cart_detail.html',{"user":user,"data":obj,"val":val})    


def category_view(request,pk):
    data=ProductCategory.objects.get(pk=pk)
    print(data) 
    return render(request,'cate.html',{"data":data})


def cart_delete(request,item_name):
    user=request.user
    print(user)
    data=Cart.objects.filter(item_name=item_name)
    data.delete()
    return redirect('/cart')


def session_add_view(request,pk):
    data=Item.objects.get(pk=pk)
    x=request.session[data.item_name]=data.item_name
    print(request.session[data.item_name])
    return redirect('cart_app:home')


def session(request):
    i=Item.objects.all()
    data=[]
    for item in i:
        if item.item_name in request.session:
            data.append(item)
    print(data)
    return render(request,'session.html',{"data":data})    


def error_view(request):
    return render(request,'error.html')  


def cart_order_view(request):
    data=request.user
    if request.method=="POST":
        data.first_name=request.POST['first_name']
        data.last_name=request.POST['last_name']
        data.address=request.POST['address']
        data.email=request.POST['email']
        data.phone_no=request.POST['phone_no']
        data.save()
        print(id)
        return redirect('cart_app:cart_order')
    return render(request,'cart_order_detail_edit.html',{"user":data})   
      

def cart_buy_view(request):
    data=Cart.objects.all()
    user=request.user
    for item in data:
        details=Item.objects.get(item_name=item.item_name)
        name=details.item_name
        price=details.item_price
        quantitie=details.quantitie
        date=datetime.date.today()
        purchase=PurchaseDetails.objects.create(name=name,price=price,quantitie=quantitie,user=user,date=date)
        purchase.save() 
        print(item.item_name)
    data.delete()
    return render(request,'success.html',{"user":user})


