
import pytest
from pypara.monetary import NoneMoney


def test_conversion_methods():
    money = NoneMoney()
    with pytest.raises(TypeError):
        float(money)
    
    with pytest.raises(TypeError):
        int(money)