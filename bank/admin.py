from django.contrib import admin
from .models import Customer, Account, Transaction

# Register your models here.
admin.site.register(Customer) 
admin.site.register(Account) 
admin.site.register(Transaction)