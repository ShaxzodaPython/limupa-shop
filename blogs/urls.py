from django.urls import path

from blogs.views import BlogsListViews, BlogsDetailViews

app_name = 'blogs'

urlpatterns = [
    path('', BlogsListViews.as_view(), name='list'),
    path('detail/<int:pk>/', BlogsDetailViews.as_view(), name='detail'),
]