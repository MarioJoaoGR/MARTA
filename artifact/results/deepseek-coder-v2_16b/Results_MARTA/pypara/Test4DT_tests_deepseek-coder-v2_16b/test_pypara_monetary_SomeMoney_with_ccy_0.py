
import pytest
from pypara.monetary import SomeMoney, Currency, NoneMoney



def test_invalid_input_with_ccy():
    with pytest.raises(TypeError):
        SomeMoney()  # Missing required arguments should raise TypeError