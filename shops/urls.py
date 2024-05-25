from django.urls import path

from shops.views import ShopsListViews

app_name = 'shops'

urlpatterns = [
    path('', ShopsListViews.as_view(), name='list'),
]