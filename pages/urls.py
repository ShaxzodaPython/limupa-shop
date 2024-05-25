from django.urls import path

from pages.views import HomePageView, ContactTemplatesView, AboutTemplatesView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactTemplatesView.as_view(), name='contact'),
    path('about/', AboutTemplatesView.as_view(), name='about'),
]
