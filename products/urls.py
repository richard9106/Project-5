from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_products, name="all_products" ),
    path('create_prouct/', views.create_product, name='create_product'),
    path('manage_product/<int:product_id>/', views.manage_product, name='manage_product'),

]
