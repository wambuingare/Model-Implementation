
# from dataclasses import Field
from datetime import datetime
from django.db import models

# Create your models here.

class Customer(models.Model):
     first_name = models.CharField(max_length=15,null=True)
     last_name = models.CharField(max_length=10,null=True)
     address = models.TextField(null=True)
     email = models.EmailField(null=True)
     phonenumber = models.CharField(max_length=10,null=True)
     age = models.PositiveSmallIntegerField(null=True)
   
     
     
class Wallet(models.Model):
     customer = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Customer,null=True)
     address = models.TextField(null=True)
     balance = models.PositiveBigIntegerField(null=True)
     transaction = models.IntegerField(null=True)
     date_created = models.DateField(default=datetime.now,null=True)
     pin = models.PositiveSmallIntegerField(null=True)
     isActive = models.BooleanField(null=True)
     currency = models.CharField(max_length=50,null=True)

class Account(models.Model):
     account_name = models.CharField(max_length=12,null=True)
     account_number = models.IntegerField(null=True)
     balance = models.IntegerField(null=True)
     description = models.TextField(null=True)

class Transaction(models.Model):
     recipient = models.URLField(null=True)
     dateandTime = models.DateTimeField(null=True)
     origin = models.ForeignKey(to=Account,on_delete=models.CASCADE,null=True)
     value = models.IntegerField(null=True)
     description = models.TextField(null=True)
     bonus_credit = models.BooleanField(null=True)
     transaction_reference = models.TextField(null=True)
     transaction_amount = models.IntegerField(null=True)

class Card(models.Model):
     cardholder_name = models.CharField(max_length=15,null=True)
     cardholder_number = models.BigIntegerField(null=True)
     expiry_date = models.DateTimeField(null=True)
     card_type = models.CharField(max_length=10,null=True)
     dateIssued = models.DateField(null=True)
     signature = models.CharField(max_length=5,null=True)
     account = models.ForeignKey(to=Customer, on_delete=models.CASCADE,null=True)
     issuer =  models.CharField(max_length=13,null=True)
     CVVcode = models.CharField(max_length=8,null=True)

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
     date_sent = models.DateField()
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
     loan_purpose = models.CharField(max_length=100,null=True)
     interest_rate = models.IntegerField()
     wallet = models.ForeignKey(null=True,on_delete=models.CASCADE,to=Wallet)
    
class Reward(models.Model):
     recipient = models.CharField(max_length=20)
     wallet = models.ForeignKey(to=Wallet,null=True,on_delete=models.CASCADE,related_name='wallet_reward')
     discount = models.IntegerField()
     points = models.SmallIntegerField()
     datetime = models.DateTimeField()
     


