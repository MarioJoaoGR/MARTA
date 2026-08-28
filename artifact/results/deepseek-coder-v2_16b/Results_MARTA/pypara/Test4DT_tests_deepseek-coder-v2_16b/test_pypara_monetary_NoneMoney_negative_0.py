
import pytest
from pypara.monetary import NoneMoney


def test_float_conversion():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        float(nm)