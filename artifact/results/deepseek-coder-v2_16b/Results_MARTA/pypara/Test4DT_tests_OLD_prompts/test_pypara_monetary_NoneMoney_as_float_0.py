
import pytest
from pypara.monetary import NoneMoney

# Test for the as_float method of NoneMoney class
def test_none_money_as_float():
    nm = NoneMoney()
    with pytest.raises(TypeError) as excinfo:
        float(nm)
    assert str(excinfo.value) == "Undefined monetary values do not have quantity information."
