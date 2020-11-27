from errors import InvalidCreditCardExpirationDate, InvalidCreditCardHolder, \
    InvalidCreditCardNumber, InvalidCreditCardSecurityCode, \
    ExpiredCreditCard, CreditCardVerificationFailed
from datetime import datetime
import re
import utils
import random


class PaymentMethod:
    @staticmethod
    def from_kwargs(**kwargs):
        if kwargs['PaymentMethod'] == 'credit_card':
            return CreditCard(
                kwargs['CreditCardNumber'],
                kwargs['CardHolder'],
                utils.parse_datetime(kwargs['ExpirationDate']),
                kwargs.get('SecurityCode')
            )
        else:
            return OtherPaymentMethod()


class OtherPaymentMethod(PaymentMethod):
    pass


class CreditCard(PaymentMethod):

    @staticmethod
    def is_valid(card_number: str):
        return bool(
            re.match(
                r'^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$',
                card_number
            )
        )

    def __init__(
            self, card_number: str, card_holder: str,
            expiration_date: datetime, security_code: str = None
    ):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.security_code = security_code

        if not CreditCard.is_valid(card_number):
            raise InvalidCreditCardNumber()
        elif not card_holder:
            raise InvalidCreditCardHolder()
        elif not expiration_date:
            raise InvalidCreditCardExpirationDate()
        elif expiration_date < datetime.now():
            raise ExpiredCreditCard()
        elif security_code and not re.match(r"^\d{3}$", security_code):
            raise InvalidCreditCardSecurityCode()
        elif not self.verify():
            raise CreditCardVerificationFailed()

    def verify(self):
        return True  # dummy verifcation, 25% verification failure
