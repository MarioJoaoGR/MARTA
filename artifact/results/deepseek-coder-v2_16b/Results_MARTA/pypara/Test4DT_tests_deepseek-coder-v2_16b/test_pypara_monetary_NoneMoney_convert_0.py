
import pytest
from pypara.monetary import NoneMoney, Currency, Date



def test_conversion_methods_on_NoneMoney():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        to_currency = Currency("USD")
        _ = nm.convert(to_currency)

def test_conversion_with_specific_date():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        to_currency = Currency("USD")
        _ = nm.convert(to_currency, asof=Date(2023, 4, 1))

def test_conversion_with_strict_mode():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        to_currency = Currency("USD")
        _ = nm.convert(to_currency, strict=True)