from django.contrib import admin
from .models import PaymentModel

# Register your models here.


@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "payment_number",
        "amount",
        "status",
        "created_date"
    )