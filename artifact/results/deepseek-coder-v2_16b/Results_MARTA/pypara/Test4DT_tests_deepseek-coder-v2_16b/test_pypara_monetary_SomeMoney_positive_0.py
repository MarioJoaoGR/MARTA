
import pytest
from datetime import date
from pypara.monetary import SomeMoney



def test_positive_method_with_negative_date():
    with pytest.raises(TypeError):
        SomeMoney(currency='USD', quantity=100, date=-date.today())

def test_positive_method_with_invalid_arguments():
    with pytest.raises(TypeError):
        SomeMoney()  # Missing required arguments should raise a TypeError