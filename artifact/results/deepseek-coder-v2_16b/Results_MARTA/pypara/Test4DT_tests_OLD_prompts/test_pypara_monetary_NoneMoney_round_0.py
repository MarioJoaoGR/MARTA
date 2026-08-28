
import pytest
from pypara.monetary import NoneMoney



def test_NoneMoney_undefined_state():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        _ = float(nm)
    with pytest.raises(TypeError):
        _ = int(nm)