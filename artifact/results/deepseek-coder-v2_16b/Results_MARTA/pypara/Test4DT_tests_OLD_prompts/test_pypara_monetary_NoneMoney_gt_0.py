
import pytest
from pypara.monetary import NoneMoney, Money

def test_valid_case():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        money1 = Money(10)  # This should raise a TypeError because NoneMoney does not accept arguments

def test_error_case():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        NoneMoney().gt(Money(10))  # This should raise a TypeError because gt method expects another Money instance
