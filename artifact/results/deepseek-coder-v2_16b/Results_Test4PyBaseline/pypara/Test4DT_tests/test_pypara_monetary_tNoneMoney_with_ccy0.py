# Module: pypara.monetary
# Import the function from the module
from pypara.monetary import NoneMoney
from decimal import Decimal

class Currency:
    def __init__(self, code):
        self.code = code

def test_with_ccy_basic():
    money_like = NoneMoney()  # Create an instance of NoneMoney
    ccy = Currency("USD")      # Create a Currency object for USD
    converted = money_like.with_ccy(ccy)  # Convert to USD using the with_ccy method
    assert isinstance(converted, NoneMoney), "Expected the result to be an instance of NoneMoney"
    assert converted.with_ccy(ccy).with_ccy(ccy) == converted, "Expected the conversion to a specific currency to return the same object"

def test_with_ccy_specific():
    money_like = NoneMoney()  # Create an instance of NoneMoney
    ccy = Currency("EUR")      # Create a Currency object for EUR
    converted = money_like.with_ccy(ccy)  # Convert to EUR using the with_ccy method
    assert isinstance(converted, NoneMoney), "Expected the result to be an instance of NoneMoney"
    assert converted.with_ccy(ccy).with_ccy(ccy) == converted, "Expected the conversion to a specific currency to return the same object"

def test_with_ccy_different():
    money_like = NoneMoney()  # Create an instance of NoneMoney
    ccy = Currency("JPY")      # Create a Currency object for JPY
    converted = money_like.with_ccy(ccy)  # Convert to JPY using the with_ccy method
    assert isinstance(converted, NoneMoney), "Expected the result to be an instance of NoneMoney"
    assert converted.with_ccy(ccy).with_ccy(ccy) == converted, "Expected the conversion to a specific currency to return the same object"
