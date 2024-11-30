import requests
import json
from django.shortcuts import redirect
from decimal import Decimal
from django.conf import settings



class SepalPaymentGateway:
    _request_url = "https://sepal.ir/api/sandbox/request.json"
    _payment_url = "https://sepal.ir/sandbox/payment/"
    _verify_url = "https://sepal.ir/api/sandbox/verify.json"
    _callback_url = "https://b113-157-90-171-202.ngrok-free.app/payment/callback/"
    

    def payment_request(self, amount, invoice_number="123"):
        payload = {
            "apiKey": "test",
            "amount": str(amount),
            "callbackUrl": self._callback_url,
            "invoiceNumber": invoice_number,
   
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.request("POST", self._request_url, headers=headers, data=json.dumps(payload))
        response_dict = json.loads(response.text)
        
        if response_dict:
            return response_dict["paymentNumber"]
        else:
            raise ValueError(f"Payment request failed: {response_dict['message']}")


    def payment_verify(self, payment_number, invoice_number="123"):
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
   
        return f"{self._payment_url}{payment_number}"
    
    
    
if __name__ == "__main__":
   
    sepal = SepalPaymentGateway()
    paymentNumber = sepal.payment_request(14000)
    print(paymentNumber)

    input("proceed to generating payment url?")

    print(sepal.generate_payment_url(paymentNumber))

    input("check the payment?")

    response = sepal.payment_verify(14000, paymentNumber)
    print(response)
    