from django.urls import path
from . import views
from .views import index, shop_view, login_view

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop_view, name='shop'),

    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('get-medicines-by-category/<int:category_id>/', views.get_medicines_by_category, name='get_medicines_by_category'),
    #path('login/', login_view, name='login'),

    path('categaris/', views.categaris, name='categaris'),
    

   
    path('protinestore/', views.protinestore, name='protinestore'),
    path('beauty/', views.beauty, name='beauty'),
    path('medicine/', views.medicine, name='medicine'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('add-to-cart/<int:medicine_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_item, name='remove_item'),
    path('payment-success/', views.dummy_payment, name='dummy_payment'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.medicine_search, name='medicine_search'),
    path('doctors/', views.doctor_list, name='doctor_list'),


]   



