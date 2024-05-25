from django.shortcuts import render
from django.views.generic import TemplateView


class ProductsListViews(TemplateView):
    template_name = 'product-sale.html'

