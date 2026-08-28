
import pytest
from pypara.monetary import NoneMoney, Currency, Money
from unittest.mock import patch

def test_valid_input():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        ccy = Currency("USD")
        nm.with_ccy(ccy)

def test_edge_case():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        with patch('pypara.monetary.NoneMoney.with_ccy', side_effect=TypeError("Conversion not supported")):
            nm.with_ccy(Currency("USD"))

def test_invalid_input():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        with patch('pypara.monetary.NoneMoney.with_ccy', side_effect=TypeError("Conversion not supported")):
            nm.with_ccy(Currency("USD"))
