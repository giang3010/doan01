from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = "home"),
    path('checkout/', views.checkout, name = "checkout"),
    path('details/', views.details, name = "details"),
    path('category', views.category, name = "category"),
    path('contact/', views.contact, name = "contact"),
    
]