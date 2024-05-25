from django.urls import path

from products.views import ProductsListViews

app_name = 'products'

urlpatterns = [
    path('', ProductsListViews.as_view(), name='list'),
]