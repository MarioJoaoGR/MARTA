
import pytest
from pypara.monetary import SomeMoney

# Test for positive_basic scenario
def test_positive_basic():
    with pytest.raises(TypeError):
        money = SomeMoney(currency='USD', quantity=100, date='2023-01-01')
