from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about_us, name='about'),
    path('search', views.search, name='search'),
    path('product', views.product_view, name='product')
]
