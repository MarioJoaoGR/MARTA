
import pytest
from pypara.monetary import Money, NoneMoney



def test_invalid_subtract():
    with pytest.raises(TypeError):
        money1 = Money(10)
        result = money1.subtract("not a Money object")