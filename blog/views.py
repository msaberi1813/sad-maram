from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from blog.forms import NameForm
# from blog.models import MyUser
from blog.models import MyUser


def home(request):
    return render(request, 'base.html', {})


def profile(request):
    f=NameForm()
    return render (request , 'register.html' , {'form':f})


def upload_file(request):
    form = NameForm(request.POST, request.FILES)
    if request.method == 'POST' :
        if form.is_valid():
                user = MyUser.objects.create_user(name=form.data['name'], email=form.data['email'],  acc_num=form.data['acc_num'])
                messages.success(request, 'ثبت نام با موفقیت انجام شد')
                user.save();
                return render(request, 'register.html', { 'user':user
                })
    return render(request, 'register.html', {'form':form})



