
import pytest
from datetime import datetime

from errors import InvalidCreditCardExpirationDate, \
    InvalidCreditCardHolder, InvalidCreditCardNumber, InvalidCreditCardSecurityCode, \
    ExpiredCreditCard
from payment_methods import CreditCard


def test_invalid_credit_card_number():
    with pytest.raises(InvalidCreditCardNumber):
        CreditCard(
            '000000000000',
            'dummy name',
            datetime(2022, 1, 31)
        )


def test_invalid_credit_card_holder():
    with pytest.raises(InvalidCreditCardHolder):
        CreditCard(
            '5500000000000004',
            None,
            datetime(2022, 1, 31)
        )


def test_invalid_credit_card_expiration_date():
    with pytest.raises(InvalidCreditCardExpirationDate):
        CreditCard(
            '5500000000000004',
            'dummy name',
            None
        )


def test_invalid_credit_card_security_code():
    with pytest.raises(InvalidCreditCardSecurityCode):
        CreditCard(
            '5500000000000004',
            'dummy name',
            datetime(2022, 1, 31),
            '0000'
        )


def test_expired_credit_card():
    with pytest.raises(ExpiredCreditCard):
        CreditCard(
            '5500000000000004',
            'dummy name',
            datetime(2020, 1, 31)
        )
