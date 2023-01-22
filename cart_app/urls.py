from django.urls import path
from.views import home_view,list,item_view,cart_view,detail_view,edit_view,buy_view,logout_view,login_view,register_view,account_view,order_view,cart_detail_view,category_view,cart_delete,session_add_view,session,error_view,cart_order_view,cart_buy_view,product_question
from django.conf import settings
from django.conf.urls.static import static

app_name="cart_app"

urlpatterns=[
    path('home/',home_view,name="home"),
    path('list/',list,name='list'),
    path('<int:pk>/',item_view),
    path('<int:pk>/cart/',cart_view),
    path('<int:pk>/detail/',detail_view,name='detail'),
    path('<int:id>/edit/',edit_view,name='edit'),
    path('<int:id>/buy/',buy_view),
    path('logout/',logout_view),
    path('login/',login_view,name='login'),
    path('register/',register_view),
    path('account/',account_view),
    path('order/',order_view),
    path('cart/',cart_detail_view),
    path('<int:pk>/cate',category_view),
    path('<str:item_name>/delete',cart_delete),
    path('<int:pk>/session_add/',session_add_view),
    path('session/',session),
    path('error/',error_view),
    path('cart_order/',cart_order_view,name="cart_order"),
    path('cart/buy',cart_buy_view),
    path('<str:category>/',product_question),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)