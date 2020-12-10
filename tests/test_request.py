import pytest

from app import app
from errors import UnsupportedPaymentMethod, InvalidCreditCardExpirationDate, \
    InvalidCreditCardHolder, InvalidCreditCardNumber, InvalidCreditCardSecurityCode, \
    ExpiredCreditCard, InvalidAmount, PaymentGatewayUnavailable


@pytest.fixture
def client():
    with app.test_client() as client:
        return client


def test_invalid_content_type(client):
    r = client.post('ProcessPayment', data={
        'PaymentMethod': 'paypal',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 19.0
    })
    assert r.status_code == 400


def test_bad_request(client):
    r = client.post('ProcessPayment', json={})
    assert r.status_code == 400


def test_unsupported_payment_method(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'paypal',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 19.0
    })
    assert r.status_code == 400
    assert r.json['type'] == UnsupportedPaymentMethod.__name__


def test_invalid_credit_card_number(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '000000000000',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 19.0
    })
    assert r.status_code == 400
    assert r.json['type'] == InvalidCreditCardNumber.__name__


def test_invalid_credit_card_holder(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': '',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 19.0
    })
    assert r.status_code == 400
    assert r.json['type'] == InvalidCreditCardHolder.__name__


def test_invalid_credit_card_expiration_date(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '00:00:00',
        'Amount': 19.0
    })
    assert r.status_code == 400
    assert r.json['type'] == InvalidCreditCardExpirationDate.__name__


def test_invalid_credit_card_security_code(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'SecurityCode': '0000',
        'Amount': 19.0
    })
    assert r.status_code == 400
    assert r.json['type'] == InvalidCreditCardSecurityCode.__name__


def test_expired_credit_card(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2020-01-31T00:00:00Z',
        'Amount': 19.0
    })
    assert r.status_code == 400
    assert r.json['type'] == ExpiredCreditCard.__name__


def test_invalid_amount(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 0.0
    })
    assert r.status_code == 400
    assert r.json['type'] == InvalidAmount.__name__


def test_valid_request_with_security_code(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'SecurityCode': '000',
        'Amount': 100.0
    })
    assert r.status_code in [200, 500]
    if r.status_code == 500:
        assert r.json['type'] == PaymentGatewayUnavailable.__name__


def test_cheap_payment_gateway(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 19.0
    })
    assert r.status_code in [200, 500]
    if r.status_code == 500:
        assert r.json['type'] == PaymentGatewayUnavailable.__name__


def test_expensive_payment_gateway(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 100.0
    })
    assert r.status_code in [200, 500]
    if r.status_code == 500:
        assert r.json['type'] == PaymentGatewayUnavailable.__name__


def test_premium_gateway(client):
    r = client.post('ProcessPayment', json={
        'PaymentMethod': 'credit_card',
        'CreditCardNumber': '5500000000000004',
        'CardHolder': 'dummy user',
        'ExpirationDate': '2022-01-31T00:00:00Z',
        'Amount': 501.0
    })
    assert r.status_code in [200, 500]
    if r.status_code == 500:
        assert r.json['type'] == PaymentGatewayUnavailable.__name__
