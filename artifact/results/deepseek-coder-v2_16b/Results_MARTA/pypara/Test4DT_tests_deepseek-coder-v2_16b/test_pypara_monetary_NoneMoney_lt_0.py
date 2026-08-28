
import pytest
from pypara.monetary import NoneMoney, Money


def test_undefined_state():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        nm < Money(100)  # This should raise TypeError since NoneMoney cannot be compared to Money directly