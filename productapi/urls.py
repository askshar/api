from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_view, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product-detail'),
]
