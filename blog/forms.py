from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.forms import ModelForm

from blog.models import MyUser, Employee
from django.contrib.auth.forms import AuthenticationForm

class AuthenticationFormWithChekUsersStatus(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.status == 'enabled':
            return 1
        else:
            return 2

class NameForm(forms.ModelForm):
    error_css_class = "error"
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "ایمیل"
        self.fields['name'].label = "نام و نام خانوادگی"
        self.fields['password'].label = "رمز عبور"
        self.fields['acc_num'].label = "شماره حساب"
        self.fields['email'].required = True
    class Meta:
        model =MyUser
        fields = ['name', 'email', 'password', 'acc_num']
        error_messages = {
            'email': {
                'unique': ('این ایمیل قبلا استفاده شده است.'),
                'required': ('وارد کردن ایمیل ضروری است'),
            }
        }
        widgets = {'password': forms.TextInput(
                     attrs={'type': 'password', 'required': True}
            ),
        }


class NameForm2(forms.ModelForm):

    class Meta:
        model =MyUser
        fields = ['name', 'email',  'acc_num' ]
        labels ={
            'email': "ایمیل",
            'name': "نام و نام خانوادگی",
            'acc_num': 'شماره حساب',

        }



class ChangePassWordForm(forms.Form):
    old_pass = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"رمز عبور")
    new_pass = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"رمز عبور جديد")
    repeat_pass = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"تکرار رمز عبور جدید")


class add_employee2(forms.ModelForm):
    class Meta:
        model =Employee
        fields = ['name', 'email',  'acc_num' , 'salary' ]
        labels ={
            'email': "ایمیل",
            'name': "نام و نام خانوادگی",
            'acc_num': 'شماره حساب',
            'salary': "حقوق",
        }

class ChangeSalary(forms.Form):
    new_salary = forms.CharField(max_length=80, widget=forms.NumberInput(), label=u"حقوق جدید")


class Nform():
    class Meta:
        pass

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()