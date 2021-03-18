from django.urls import path

from .views import ProductsList, ProductDetail


urlpatterns = [
    path('', ProductsList.as_view(), name='products-list'),
    path('<int:product_id>', ProductDetail.as_view(), name='product_detail')
]