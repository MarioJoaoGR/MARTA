
import pytest
from pypara.monetary import NoneMoney, Money


def test_undefined_vs_undefined():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert money1.gte(money2) == True  # both are undefined, so gte should return True



