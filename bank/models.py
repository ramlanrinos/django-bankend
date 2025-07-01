from django.db import models

# Create your models here.
class Customer(models.Model): 
    name = models.CharField(max_length=100) 
    dob = models.DateField() 
    email = models.EmailField(unique=True) 
    address = models.TextField() 
 
    def __str__(self): 
        return self.name
    
class Account(models.Model): 
    ACCOUNT_TYPES = [ 
        ('SAV', 'Savings'), 
        ('CUR', 'Current'), 
    ] 
 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPES) 
    balance = models.DecimalField(max_digits=12, decimal_places=2) 
    created_at = models.DateField(auto_now_add=True) 
 
    def __str__(self): 
        return f"{self.customer.name} - {self.account_type}"

class Transaction(models.Model): 
    account = models.ForeignKey(Account, on_delete=models.CASCADE) 
    TRANSACTION_TYPES = [ 
        ('D', 'Deposit'), 
        ('W', 'Withdrawal'), 
    ] 
    transaction_type = models.CharField(max_length=1, 
choices=TRANSACTION_TYPES) 
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    timestamp = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return f"{self.get_transaction_type_display()} of {self.amount} on {self.timestamp}" 