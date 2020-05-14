from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User, auth
from .models import NHOM_SP, DANHMUC_SP, SANPHAM


# Create your views here.
def index(request):
    itemnhom = NHOM_SP.objects.all()
    return render(request, 'index.html',{'itemnhom':itemnhom})

def checkout(request):
    return render(request, 'checkout.html')
    
def contact(request):
    return render(request, 'contact.html')

def category(request):
    itemsp = SANPHAM.objects.all()
    return render(request, 'category.html',{'itemsp':itemsp})

def category_details(request,id_sanpham):
    sanpham = SANPHAM.objects.get(pk = id_sanpham)
    return render(request, 'details.html',{'sanpham': sanpham})

def details(request,id_sanpham):
    if id_sanpham:
        # try:    
        sanpham = SANPHAM.objects.get(pk = id_sanpham)
        # except SANPHAM.DoesNotExist:
        #     raise Http404("Lỗi")
        return render(request, 'details.html',{'sanpham': sanpham})
    else:
        return render(request, 'details.html',{})
    
def view_details(request):
        return render(request, 'details.html',{})

def base(request):
    itemdm = DANHMUC_SP.objects.filter(MaNhom=1)
    print(itemdm.TenDM)
    itemnhom = NHOM_SP.objects.all()
    context = {
        'itemdm' : itemdm,
        'itemnhom' : itemnhom,
    }
    return render(request, 'base.html',context)


