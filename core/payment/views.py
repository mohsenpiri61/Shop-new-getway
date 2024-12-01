from django.views.generic import View
from .models import PaymentModel, PaymentStatusType
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .sepal import SepalPaymentGateway
from order.models import OrderModel, OrderStatusType


class PaymentCallbackView(View):
    def get(self, request, *args, **kwargs):
        # دریافت پارامترهای ارسال شده به مرورگر
        full_path = request.get_full_path()  # دریافت مسیر کامل URL
        payment_number = full_path.rstrip('/').split('/')[-1]  # استخراج بخش آخر
        print(f"Payment Number: {payment_number}")  # نمایش در کنسول
        
        payment_obj = get_object_or_404(PaymentModel, payment_number=payment_number)
        
       
        sepal = SepalPaymentGateway() 
        response = sepal.payment_verify(int(payment_obj.amount), payment_obj.payment_number)
        
        status_code = response.get("status", 3)
        
        payment_obj.response_code = status_code
        payment_obj.status = PaymentStatusType.success.value if status_code in {
            100, 101} else PaymentStatusType.failed.value
        payment_obj.response_json = response
        payment_obj.save()

        order = OrderModel.objects.get(payment=payment_obj)
        order.status = OrderStatusType.PAID.value if status_code in {
            100, 101} else OrderStatusType.CANCELED.value
        order.save()
        
        return redirect(reverse_lazy("order:completed") if status_code in {100, 101} else reverse_lazy("order:failed"))

