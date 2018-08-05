from khayyam import *
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email,acc_num="0",  name = "ناشناس", password=None ):
        if not email:
            raise ValueError('وارد کردن ایمیل ضروری است!')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            name = name,

            acc_num = acc_num,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        user = self.create_user(email,
                                password=password,
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user





class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True , null=False , blank=False)
    name = models.CharField(max_length=50 , default="ناشناس" , null=True, blank=True)
    acc_num =  models.CharField(max_length=30 , null=False, blank=False)
    rial_wallet=models.IntegerField(default=0)
    dollar_wallet=models.IntegerField(default=0)
    euro_wallet=models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def get_full_name(self):
        return self.name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Employee(MyUser):
    salary = models.IntegerField(default=0)

class Manager(MyUser):
    dollor_account =  models.CharField(max_length=30 , null=False , default="موضوع");
    euro_account = models.CharField(max_length=30 , null=False)

class Transaction(models.Model):
    date = models.DateTimeField(default=timezone.now())
    type = models.CharField(max_length=30 , null=False , default="");
    status = models.CharField(max_length=30 , null=False , default="در حال انتظار");
    employee = models.ForeignKey(Employee , on_delete = models.CASCADE , related_name='karmand')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE , related_name='karbar')
    subject =   models.CharField(max_length=30 , null=False , default="موضوع");
    content =  models.CharField(max_length=300 , null=False , default="محتوا");

class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , blank=True, null=True,related_name='ferestande')
    created_date = models.DateTimeField(default=timezone.now())
    reciever =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , blank=True, null=True,related_name='girande')
    subject =  models.CharField(max_length=30 , null=False , default="موضوع");
    content =  models.CharField(max_length=300 , null=False , default="محتوا");
    transaction = models.ForeignKey( Transaction , on_delete=models.CASCADE, blank=True, null=True)

