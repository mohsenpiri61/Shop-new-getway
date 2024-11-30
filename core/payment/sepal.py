import requests
from django.shortcuts import redirect
from decimal import Decimal
from django.conf import settings



class SepalPaymentGateway:
    _request_url = "https://sepal.ir/api/sandbox/request.json"
    _payment_url = "https://sepal.ir/sandbox/payment/"
    _verify_url = "https://sepal.ir/api/sandbox/verify.json"
    _callback_url = "http://127.0.0.1:8000/"
    

    def payment_request(self, amount, invoice_number="123"):
        """
        ارسال درخواست پرداخت به سپال.
        """
        payload = {
            "apiKey": "test",
            "amount": str(amount),
            "callbackUrl": self._callback_url,
            "invoiceNumber": invoice_number,
   
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.request("POST", self._request_url, headers=headers, data=json.dump(payload))
        response_dict = json.loads(response.text)
        if "data" in response_dict and response_dict["data"]:
            return response_dict["data"]["paymentNumber"]
        else:
            raise ValueError(f"Payment request failed: {response_dict['errors']}")


    def payment_verify(self, payment_number, invoice_number):
        """
        بررسی وضعیت پرداخت.
        """
        payload = {
            "apiKey": "test",
            "paymentNumber": payment_number,
            "invoiceNumber": str(invoice_number),
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(self._verify_url, headers=headers, data=json.dumps(payload))
        return response.json()

    def generate_payment_url(self, payment_number):
        """
        تولید لینک پرداخت.
        """
        return f"{self._payment_url}{payment_number}"