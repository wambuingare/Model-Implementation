from django.contrib import admin
from.models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notification,Receipt,Loan,Reward

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):    
   list_display = ("first_name","last_name","address",)
   search_fields = ("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
   list_display = ("customer","address","balance","transaction","date_created","pin","isActive","currency",)
   search_fields = ("customer","address","date_created",)
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):    
   list_display = ("account_name","account_number","balance","description",)
   search_fields = ("account_name","account_number","balance",)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):    
   list_display = ("recipient","dateandTime","origin","value","description","bonus_credit","transaction_reference","transaction_amount",)
   search_fields = ("bonus_credit","transaction_amount",)
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):    
   list_display = ("cardholder_name","cardholder_number","expiry_date","card_type","dateIssued","signature","account","issuer","CVVcode",)
   search_fields = ("cardholder_name","expiry_date","dateIssued",)
admin.site.register(Card,CardAdmin)


class ThirdPartyAdmin(admin.ModelAdmin):    
   list_display = ("name","gender","account","location","transaction_cost","currency",)
   search_fields = ("name","location","currency",)
admin.site.register(ThirdParty,ThirdPartyAdmin)


class NotificationAdmin(admin.ModelAdmin):    
   list_display = ("name","message","dateandTime","date_sent","status",)
   search_fields = ("name","date_sent","status",)
admin.site.register(Notification,NotificationAdmin)


class ReceiptAdmin(admin.ModelAdmin):    
   list_display = ("first_name","last_name","amount","datetime","receipt_number","description","receipt_type",)
   search_fields = ("first_name","datetime","receipt_number",)
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):    
   list_display = ("name","payment_due_date","loan_term","loan_balance","dateissue","amount","interest_rate","wallet",)
   search_fields = ("name","loan_term","loan_balance",)
admin.site.register(Loan,LoanAdmin)


class RewardAdmin(admin.ModelAdmin):    
   list_display = ("recipient","wallet","discount","points","datetime",)
   search_fields = ("recipient","points","datetime",)
admin.site.register(Reward,RewardAdmin)


