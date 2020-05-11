from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = "home"),
    path('checkout/', views.checkout, name = "checkout"),
    path('register/', views.register, name = "register"),
    path('details/', views.details, name = "details"),
    path('products/', views.products, name = "products"),
    path('contact/', views.contact, name = "contact"),
    
]