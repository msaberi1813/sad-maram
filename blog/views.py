from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from blog.forms import NameForm, NameForm2, Nform, ChangePassWordForm, add_employee2
# from blog.models import MyUser
from blog.models import MyUser, Employee


def home(request):
    return render(request, 'base.html', {})


def profile(request):
    f=NameForm()
    return render (request , 'register.html' , {'form':f})

@login_required
def edit(request):
    f=NameForm2(instance=request.user)
    return render (request , 'profile_edit_user.html' , {'form':f , 'user': request.user})
@login_required
def bala_pass(request):
    f=ChangePassWordForm(request.POST)
    return render (request , 'change_password.html' , {'form':f})

def bala_add_employee(request):
    f=add_employee2(request.POST , instance=request.user)
    return render (request , 'add_employee.html' , {'form':f , 'user': request.user})

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

@login_required
def edit_user_profile(request):
    form = NameForm2(request.POST)

    if request.method == 'POST' :
        if form.is_valid():
            user =  MyUser.objects.get(pk = request.user.pk)
            user.name = form.cleaned_data['name']
            user.acc_num = form.cleaned_data['acc_num']
            try:
                user.email = form.cleaned_data['email']
            except:
                pass
            messages.success(request, 'ویرایش با موفقیت انجام شد')
            user.save()
            return render(request, 'profile_edit_user.html', {})
        else:
            user =  MyUser.objects.get(pk = request.user.pk)
            user.name = form.cleaned_data['name']
            user.acc_num = form.cleaned_data['acc_num']
            messages.success(request, 'ویرایش با موفقیت انجام شد')
            user.save()
            return render(request, 'profile_edit_user.html', {})

    return render(request, 'profile_edit_user.html', {'form':form})



@login_required
def change_pass(request):
    form = ChangePassWordForm(request.POST)
    if request.method == 'POST' :
        if form.is_valid():
            u = MyUser.objects.get(pk=request.user.pk)
            if u.password == form.cleaned_data['old_pass'] and form.cleaned_data['new_pass'] == form.cleaned_data['repeat_pass']  :
                u.set_password(form.cleaned_data['new_pass'])
                u.save()
                messages.success(request, 'تغییر رمز با موفقیت انجام شد')
                u.save()
                return render(request, 'change_password.html', {})
            else:
                messages.success(request, 'ورودی های خود را چک کنید')
    return render(request, 'change_password.html', {'form':form})

def add_employee(request):
    form = add_employee2(request.POST)
    if request.method == 'POST':
        print("hhhhhhhhhhhhhhhhhhhhhhhhh")
        if form.is_valid():
            print("yeeeeeeeeeeeeeeeeeeeeeeeees")
            user = form.save()
            user.set_password('123456')
            user.save()
            messages.success(request, 'ثبت کارمند با موفقیت انجام شد')
            return render(request, 'add_employee.html', {'user': user, 'form':form})

        return render(request, 'add_employee.html', {'form': form})

