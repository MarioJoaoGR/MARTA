
import pytest
from pypara.monetary import NoneMoney

# Test that as_float method raises TypeError when called on an instance of NoneMoney
def test_as_float_raises_type_error():
    nm = NoneMoney()
    with pytest.raises(TypeError) as e:
        nm.as_float()
    assert str(e.value) == "Undefined monetary values do not have quantity information."

# Test that converting an instance of NoneMoney to float raises TypeError
def test_float_conversion_raises_type_error():
    nm = NoneMoney()
    with pytest.raises(TypeError) as e:
        float(nm)
    assert str(e.value) == "Undefined monetary values do not have quantity information."

# Test evaluation of a NoneMoney instance in boolean context, which should be False
def test_none_money_instance_evaluation():
    nm = NoneMoney()
    assert bool(nm) is False
