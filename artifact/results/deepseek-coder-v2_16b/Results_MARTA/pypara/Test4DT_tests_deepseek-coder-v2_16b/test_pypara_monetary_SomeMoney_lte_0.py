
import pytest
from pypara.monetary import SomeMoney



def test_invalid_currency():
    with pytest.raises(TypeError):
        SomeMoney(100, None)
