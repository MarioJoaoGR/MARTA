
import pytest
from pypara.monetary import NonePrice, NoMoney



def test_nonemoney_arithmetic():
    with pytest.raises(TypeError):
        nm = NoMoney() + NoMoney()
