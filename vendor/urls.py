from django.urls import path
from. import views

urlpatterns = [
    path('vendors/', views.vendor_list_view, name='vendor_list'), 
    path('<vendor_id>/', views.vendor_view, name='vendor_list') 
]

