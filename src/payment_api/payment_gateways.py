from payment_methods import PaymentMethod, CreditCard
from errors import UnsupportedPaymentMethod, InvalidAmount, PaymentGatewayUnavailable
import random


class PaymentGateway:
    def __init__(self):
        self.is_available = random.choice([True, False])  # dummy checking if available, 50% chance to fail

    def pay(self, amount: float, payment_method: PaymentMethod):
        if isinstance(payment_method, CreditCard):
            if amount <= 0:
                raise InvalidAmount(amount)
            elif not self.is_available:
                raise PaymentGatewayUnavailable(self)
            else:
                return f'successfully paid via {self.__class__.__name__}'
        else:
            raise UnsupportedPaymentMethod(payment_method)


class CheapPaymentGateway(PaymentGateway):
    pass


class ExpensivePaymentGateway(PaymentGateway):
    pass


class PremiumPaymentGateway(PaymentGateway):
    pass


def process_payment(amount: float, payment_method: PaymentMethod):
    if int(amount) == 20 or amount <= 0:
        raise InvalidAmount(amount)
    elif amount < 20:
        return CheapPaymentGateway().pay(amount, payment_method)
    elif amount <= 500:
        try:
            return ExpensivePaymentGateway().pay(amount, payment_method)
        except PaymentGatewayUnavailable:
            return CheapPaymentGateway().pay(amount, payment_method)
    else:
        error = None
        for _ in range(3):
            try:
                payment_gateway = PremiumPaymentGateway()
                return payment_gateway.pay(amount, payment_method)
            except PaymentGatewayUnavailable as ex:
                error = ex
        else:
            raise error
    e
