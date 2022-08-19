
from dataclasses import Field
from datetime import datetime
from locale import currency
import mailcap
from pyexpat import model
from django.db import models

# Create your models here.

class Customer(models.Model):
     first_name = models.CharField(max_length=15)
     last_name = models.CharField(max_length=10)
     address = models.TextField()
     email = models.EmailField()
     phonenumber = models.CharField(max_length=10)
     age = models.PositiveSmallIntegerField()
     
class Wallet(models.Model):
     customer = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Customer)
     address = models.TextField()
     balance = models.PositiveBigIntegerField()
     transaction = models.IntegerField()
     date_created = models.DateField(default=datetime.now)
     pin = models.PositiveSmallIntegerField()
     isActive = models.BooleanField()
     currency = models.CharField(max_length=50)

class Account(models.Model):
     account_name = models.CharField(max_length=12)
     account_number = models.IntegerField()
     balance = models.IntegerField()
     transaction = models.CharField(max_length=100)
     description = models.TextField()

class Transaction(models.Model):
     recipient = models.URLField()
     dateandTime = models.DateTimeField()
     source = models.URLField()
     value = models.IntegerField()
     description = models.TextField()
     bonus_credit = models.BooleanField()
     transaction_reference = models.TextField()
     transaction_amount = models.IntegerField()

class Card(models.Model):
     cardholder_name = models.CharField(max_length=15)
     cardholder_number = models.BigIntegerField()
     expirydate = models.DateTimeField()
     card_type = models.CharField(max_length=10)
     dateIssued = models.DateField()
     signature = models.CharField(max_length=5)
     account = models.ManyToManyField(to=Customer)
     issuer =  models.CharField(max_length=13)
     CVVcode = models.CharField(max_length=8)

class ThirdParty(models.Model):
     name = models.CharField(max_length=18)
     gender = models.CharField(max_length=10)
     account = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
     location = models.CharField(max_length=20)
     transaction_cost = models.IntegerField()
     currency = models.CharField(max_length=5)

class Notification(models.Model):
     name = models.CharField(max_length=10)
     message = models.TextField()
     dateandTime = models.DateTimeField()
     dateSent = models.DateField()
     status = models.BooleanField()

class Receipt(models.Model):
     first_name = models.CharField(max_length=12)
     last_name = models.CharField(max_length=10)
     amount = models.BigIntegerField()
     datetime = models.DateTimeField()
     receipt_number = models.CharField(max_length=8)
     description = models.TextField()
     receipt_type = models.CharField(max_length=9)
   
class Loan(models.Model):
     name = models.CharField(max_length=20)
     payment_due_date = models.DateTimeField(default=datetime.now)
     loan_term = models.IntegerField(null=True)
     loan_balance = models.IntegerField(null=True)
     dateissue = models.DateTimeField(default=datetime.now)
     amount = models.BigIntegerField(null=True)
     Loan_purpose = models.CharField(max_length=100,null=True)
     Interest_rate = models.IntegerField()
     Wallet = models.ForeignKey(null=True,on_delete=models.CASCADE,to=Wallet)
    
class Reward(models.Model):
     name = models.CharField(max_length=20)
     recipient = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
     discount = models.IntegerField()
     points = models.SmallIntegerField()
     tickets = models.CharField(max_length=8)
     coupons = models.CharField(max_length=10)
     datetime = models.DateTimeField()
     


