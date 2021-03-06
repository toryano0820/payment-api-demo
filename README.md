**<h1>Payment API</h1>**

**<h2>Installing dependencies</h2>**
- execute **`pip install -r requirements.txt`**

___
**<h2>Starting API</h2>**
- execute **`python src/app.py`**

___
**<h2>Request Specs</h2>**
- *Path*:         **`/ProcessPayment`**
- *Method*:       **`POST`**
- *Content Type*: **`application/json`**
- *Request Body*:
```
{
    "PaymentMethod":    "<string>",   // currently, "credit_card" is only allowed
    "CreditCardNumber": "<string>",   // accepts any valid credit card number
    "CardHolder":       "<string>",   // cannot be empty
    "ExpirationDate":   "<datetime>", // "yyyy-MM-ddTHH:mm:ss.fffZ", "yyyy-MM-ddTHH:mm:ssZ", "yyyy-MM-dd", "MM/yy", "MM-yy", or "MMyy"
    "SecurityCode":     "<string>",   // 3 digit security code, optional
    "Amount":           "<decimal>"   // accepts decimal numbers greater than 0.0
}
```
___
**<h2>Testing</h2>**
- execute **`pytest -v src\app.py ..`**
