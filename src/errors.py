import re


class UnsupportedPaymentMethod(ValueError):
    def __init__(self, payment_method):
        super().__init__(f'unsupported payment method {payment_method.__class__.__name__}')


class InvalidCreditCard(ValueError):
    def __init__(self):
        super().__init__(' '.join(re.findall(r'[A-Z][^A-Z]*', self.__class__.__name__)).lower())


class InvalidCreditCardNumber(InvalidCreditCard):
    pass


class InvalidCreditCardHolder(InvalidCreditCard):
    pass


class InvalidCreditCardExpirationDate(InvalidCreditCard):
    pass


class InvalidCreditCardSecurityCode(InvalidCreditCard):
    pass


class ExpiredCreditCard(InvalidCreditCard):
    pass


class CreditCardVerificationFailed(InvalidCreditCard):
    pass


class InvalidAmount(ValueError):
    def __init__(self, amount):
        super().__init__(f'invalid amount: {amount}')


class PaymentGatewayUnavailable(ConnectionError):
    def __init__(self, payment_gateway, *args):
        super().__init__(f'unable to process request via {payment_gateway.__class__.__name__}')
