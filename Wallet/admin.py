from django.contrib import admin
from.models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notification,Receipt,Loan,Reward

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):    
   list_display = ("first_name","last_name","address",)
   search_fields = ("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)


