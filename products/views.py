from django.shortcuts import render
from django.views.generic import ListView
from products.models import ProductModel


class ProductsListViews(ListView):
    template_name = 'product-list.html'
    model = ProductModel
    context_object_name = 'products'

