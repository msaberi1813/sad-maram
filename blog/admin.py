from django.contrib import admin
from .models import MyUser, Transaction, Message, Employee

admin.site.register(MyUser)
admin.site.register(Employee)
admin.site.register(Transaction)
admin.site.register(Message)