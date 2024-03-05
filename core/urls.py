from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.index_view, name='index'),
    path('cart/', views.cart_view, name='cart_page'),
    path('checkout/', views.checkout_view, name='checkout_page'),
    path('product/<product_id>/', views.product_view, name='product_page'),
    path('order/', views.order_view, name='order_page'),
    path('wishlist/', views.wishlist_view, name='wishlist_page'),
    path('category/<category_id>/', views.category_view, name='category_page')
    ]