from django.contrib import admin
from .models.balance import Balance
from .models.transaction import Transaction
# Register your models here.
admin.site.register(Balance)
admin.site.register(Transaction)

