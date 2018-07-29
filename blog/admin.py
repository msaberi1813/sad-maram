from django.contrib import admin
from .models import MyUser, Transaction, Message

admin.site.register(MyUser)
admin.site.register(Transaction)
admin.site.register(Message)