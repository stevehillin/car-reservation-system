import os
from app import app

class PaymentProcessor():

    def __init__(self):
        merchant_id = os.environ.get("MERCHANT_ID")
        # TODO: Implement Payment Gateway

    def _luhn_checksum(self, card_number):
        def digits_of(card_number):
            return [int(d) for d in str(card_number)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10

    def ValidateCard(self, card_number) -> bool:
        return self._luhn_checksum(card_number) == 0

    # TODO:  Add methods needed to charge credit cards, issue refunds, etc.