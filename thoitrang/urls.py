from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = "home"),
    path('checkout/', views.checkout, name = "checkout"),
    path('details/<id_sanpham>', views.details, name = "details"),
    path('category/', views.category, name = "category"),
    path('contact/', views.contact, name = "contact"),
    path('base', views.base, name = "base"),
    path('details/', views.view_details, name = "detail"),
    path('category/details/<id_sanpham>', views.category_details, name = "details"),
]