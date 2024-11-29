from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    FormView,
    View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from order.permissions import HasCustomerAccessPermission
from order.models import UserAddressModel
from order.forms import CheckOutForm
from cart.models import CartModel, CartItemModel
from order.models import OrderModel, OrderItemModel
from django.urls import reverse_lazy
from cart.cart import CartSession
from decimal import Decimal
from order.models import CouponModel
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import redirect
from payment.zarinpal_client import ZarinPalSandbox
from payment.models import PaymentModel
from decimal import Decimal

class OrderCheckOutView(LoginRequiredMixin, HasCustomerAccessPermission, FormView):
    template_name = "order/checkout.html"
    form_class = CheckOutForm
    success_url = reverse_lazy('order:completed')

    def get_form_kwargs(self):
        kwargs = super(OrderCheckOutView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        
        cleaned_data = form.cleaned_data
        address = cleaned_data['address_id']
        coupon = cleaned_data['coupon']

        cart = CartModel.objects.get(user=self.request.user)
        cart_items = cart.cart_items.all()
        order = OrderModel.objects.create(
            user=self.request.user,
            address=address.address,
            state=address.state,
            city=address.city,
            zip_code=address.zip_code,
        )
        for item in cart_items:
            OrderItemModel.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.get_price())
            
        cart_items.delete()
        
        CartSession(self.request.session).clear()
        total_price = order.calculate_total_price()
        if coupon:
            total_price = total_price - round((total_price * Decimal(coupon.discount_percent/100)))
        order.total_price = order.calculate_total_price()
        order.save()
         
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(
            user=self.request.user)
        total_price = cart.calculate_total_price()
        context["total_price"] = total_price
        context["total_tax"] = round((total_price * 9)/100)
        return context


class OrderCompletedView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "order/completed.html"
    
class OrderFailedView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "order/failed.html"


class ValidateCouponView(LoginRequiredMixin, HasCustomerAccessPermission, View):

    def post(self, request, *args, **kwargs):
        code = request.POST.get("code")
        user = self.request.user

        status_code = 200
        message = "کد تخفیف با موفقیت ثبت شد"
        total_price = 0
        total_tax = 0

        try:
            coupon = CouponModel.objects.get(code=code)
        except CouponModel.DoesNotExist:
            return JsonResponse({"message": "کد تخفیف یافت نشد"}, status=404)
        else:
            if coupon.used_by.count() >= coupon.max_limit_usage:
                status_code, message = 403, "محدودیت در تعداد استفاده"

            elif coupon.expiration_date and coupon.expiration_date < timezone.now():
                status_code, message = 403, "کد تخفیف منقضی شده است"

            elif user in coupon.used_by.all():
                status_code, message = 403, "این کد تخفیف قبلا توسط شما استفاده شده است"

            else:
                cart = CartModel.objects.get(user=self.request.user)

                total_price = cart.calculate_total_price()
                total_price = round(
                    total_price - (total_price * (coupon.discount_percent/100)))
                total_tax = round((total_price * 9)/100)
        return JsonResponse({"message": message, "total_tax": total_tax, "total_price": total_price}, status=status_code)
