**<h1>Payment API</h1>**

**<h2>Installing dependencies</h2>**
- For API, execute **`pip install flask`**
- For testing, execute **`pip install flask pytest`**

___
**<h2>Starting API</h2>**
- execute **`python src/payment_api/app.py`**

___
**<h2>Request Specs</h2>**
- *Path*:         **`/ProcessPayment`**
- *Method*:       **`POST`**
- *Content Type*: **`application/json`**
- *Request Body*:
```
{
    "PaymentMethod":    "<string>",   // currently, "credit_card" is only allowed
    "CreditCardNumber": "<strimg>",   // accepts any valid credit card number
    "CardHolder":       "<string>",   // cannot be empty
    "ExpirationDate":   "<datetime>", // "yyyy-MM-ddTHH:mm:ss.fffZ", "yyyy-MM-ddTHH:mm:ssZ", "yyyy-MM-dd", "MM/yy", "MM-yy", or "MMyy"
    "SecurityCode":     "<string>",   // 3 digit security code, optional
    "Amount":           "<decimal>"   // accepts decimal numbers greater than 0.0
}
```
___
**<h2>Testing</h2>**
- execute **`pytest -v`**