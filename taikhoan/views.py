from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth

def register1(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Tài khoản đã tồn tại!')
                return redirect('register1')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email đã được sử dụng!')
                return redirect('register1')
            else:
                user = User.objects.create_user(username = username, password= password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'Tạo tài khoản thành công!')
                return HttpResponseRedirect(reverse('login1'))
        else:
            messages.info(request,'Mật khẩu không trùng khớp!')
            return redirect('register1')
        return redirect('/')
    else:
        return render(request,'register1.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Thông tin không hợp lệ')
            return redirect('login1')
    else:
        return render(request,'login1.html')

def logout(request):
    auth.logout(request)
    return redirect('/')