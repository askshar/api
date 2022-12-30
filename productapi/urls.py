from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.Products.as_view(), name='all-products'),
    path('products/<pk>/', views.ProductDetail.as_view(), name='product-details'),
]
