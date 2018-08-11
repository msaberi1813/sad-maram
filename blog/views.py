from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from blog.forms import NameForm, NameForm2, Nform, ChangePassWordForm, add_employee2, ChangeSalary
# from blog.models import MyUser
from blog.models import MyUser, Employee, Transaction


def profile(request):
    f=NameForm()
    return render (request , 'register.html' , {'form':f})

@login_required(redirect_field_name='login')
def edit(request):
    f=NameForm2(instance=request.user)
    return render (request , 'profile_edit_user.html' , {'form':f , 'user': request.user})


@login_required(redirect_field_name='login')
def bala_edit_emp(request):
    f=NameForm2(instance=request.user)
    return render (request , 'profile_edit_employee.html' , {'form':f , 'user': request.user})



@login_required(redirect_field_name='login')
def bala_edit_manager(request):
    f=NameForm2(instance=request.user)
    return render (request , 'profile_edit_manager.html' , {'form':f , 'user': request.user})


@login_required(redirect_field_name='login')
def bala_pass(request):
    f=ChangePassWordForm(request.POST)
    return render (request , 'change_password.html' , {'form':f})

@login_required(redirect_field_name='login')
def bala_add_employee(request):
    f=add_employee2(instance=request.user)
    return render (request , 'add_employee.html' , {'form':f , 'user': request.user})

def upload_file(request):
    form = NameForm(request.POST, request.FILES)
    if request.method == 'POST' :
        if form.is_valid():
                user = form.save();
                user.set_password(form.data['password'])
                # user = MyUser.objects.create_user(name=form.data['name'], email=form.data['email'],  acc_num=form.data['acc_num'])
                messages.success(request, 'ثبت نام با موفقیت انجام شد')
                user.save();
                return render(request, 'register.html', { 'user':user
                })
    return render(request, 'register.html', {'form':form})

@login_required(redirect_field_name='login')
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


@login_required(redirect_field_name='login')
def edit_employee_profile(request):
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
            return render(request, 'profile_edit_employee.html', {})

    return render(request, 'profile_edit_employee.html', {'form':form})


@login_required(redirect_field_name='login')
def edit_manager_profile(request):
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
            return render(request, 'profile_edit_manager.html', {})

    return render(request, 'profile_edit_manager.html', {'form':form})

@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
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

def employee_list(request):
    employees = Employee.objects.all()
    print("fffffffffffffffffffffffffffffffff   ")
    print(employees)
    return render(request, 'employee_list.html',{'employees':employees} )

def usr_list(request):
    employees = MyUser.objects.all()

    return render(request, 'usr_list.html',{'employees':employees} )


def see_employee_profile(request, pke):
    e = Employee.objects.filter(pk = pke).first()
    return render(request, 'employee_profile.html' , {'e': e})

def see_usr_profile(request, pke):
    e = MyUser.objects.filter(pk = pke).first()
    return render(request, 'usr_profile.html' , {'e': e})

def bala_change_employee_salary(request,pke):
    form = ChangeSalary(request.POST)

    u = Employee.objects.get(pk=pke)

    return render(request, 'change_employee_salary.html' ,{'form':form , 'e':u} )

def change_salary(request , pke):
    form = ChangeSalary(request.POST)
    if request.method == 'POST' :
        if form.is_valid():
            u = Employee.objects.get(pk=pke)
            u.salary = form.data['new_salary']
            u.save()
            messages.success(request, 'تغییر حقوق با موفقیت انجام شد')
            return render(request, 'change_employee_salary.html', {'form':form , 'e':u})
        else:
                messages.success(request, 'ورودی های خود را چک کنید')
    return render(request, 'change_employee_salary.html', {'form':form })


def ban_employee(request, pke):
    pass #todo

def see_employee_transactions(request, pke):
    e = Employee.objects.filter(pk = pke).first()
    t = Transaction.objects.filter(employee = e)
    return render(request, 'employee_transactions.html', {'transactions': t , 'e':e})


def see_usr_transactions(request, pke):
    e = MyUser.objects.filter(pk = pke).first()
    t = Transaction.objects.filter(employee = e)
    return render(request, 'usr_transactions.html', {'transactions': t , 'e':e})


def see_transaction_context(request, pkt):
    t = Transaction.objects.filter(pk = pkt).first()
    return render(request , 'transaction_context.html' , {'t':t})

def nerkh_arz(request):
    response = requests.get('https://www.faranevis.com/api/currency/')
    geodata = response.json()
    return render(request, 'nerkh_arz.html', {
        'dollar': geodata['دلار'],
        'euro': geodata['یورو'],
    })