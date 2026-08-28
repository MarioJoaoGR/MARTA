
import pytest
from pypara.monetary import NoneMoney

def test_scalar_subtract_with_numeric():
    nm = NoneMoney()
    result = nm.scalar_subtract(5)
    assert isinstance(result, NoneMoney), "Expected the result to be an instance of NoneMoney"

def test_scalar_subtract_with_none_money():
    nm1 = NoneMoney()
    nm2 = NoneMoney()
    result = nm1.scalar_subtract(nm2)
    assert isinstance(result, NoneMoney), "Expected the result to be an instance of NoneMoney"

def test_scalar_subtract_with_defined_numeric():
    nm = NoneMoney()
    result = nm.scalar_subtract(100.25)
    assert isinstance(result, NoneMoney), "Expected the result to be an instance of NoneMoney"
