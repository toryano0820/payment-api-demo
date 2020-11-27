
import os
import pytest
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src/payment_api'))

from errors import InvalidAmount, PaymentGatewayUnavailable, UnsupportedPaymentMethod
from payment_methods import CreditCard, OtherPaymentMethod
from payment_gateways import process_payment


def test_invalid_amount():
    with pytest.raises(InvalidAmount):
        process_payment(
            0.0,
            CreditCard(
                '5500000000000004',
                'dummy user',
                datetime(2022, 1, 31)
            )
        )


def test_unsupported_payment_method():
    with pytest.raises(UnsupportedPaymentMethod):
        process_payment(100.0, OtherPaymentMethod())


def test_cheap_payment_gateway():
    try:
        msg = process_payment(
            19.0,
            CreditCard(
                '5500000000000004',
                'dummy user',
                datetime(2022, 1, 31)
            )
        )
        assert isinstance(msg, str)
    except Exception as ex:
        assert isinstance(ex, PaymentGatewayUnavailable)


def test_expensive_payment_gateway():
    try:
        msg = process_payment(
            100.0,
            CreditCard(
                '5500000000000004',
                'dummy user',
                datetime(2022, 1, 31)
            )
        )
        assert isinstance(msg, str)
    except Exception as ex:
        assert isinstance(ex, PaymentGatewayUnavailable)


def test_premium_payment_gateway():
    try:
        msg = process_payment(
            501.0,
            CreditCard(
                '5500000000000004',
                'dummy user',
                datetime(2022, 1, 31)
            )
        )
        assert isinstance(msg, str)
    except Exception as ex:
        assert isinstance(ex, PaymentGatewayUnavailable)
