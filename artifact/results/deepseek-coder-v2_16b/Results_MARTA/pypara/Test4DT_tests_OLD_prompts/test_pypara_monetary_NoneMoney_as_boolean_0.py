
import pytest
from pypara.monetary import NoneMoney

# Test 1: Initialization of NoneMoney object
def test_none_money_initialization():
    nm = NoneMoney()
    assert isinstance(nm, NoneMoney), "Expected instance to be of type NoneMoney"

# Test 2: Boolean evaluation of NoneMoney object
def test_none_money_as_boolean():
    nm = NoneMoney()
    assert bool(nm) is False, "Expected bool(NoneMoney()) to be False"

# Test 3: Comparison operations with NoneMoney objects
def test_none_money_comparison():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert money1 == money2, "Expected comparison between two undefined NoneMoney objects to be True (equivalent)"

# Test 4: Conversion methods for NoneMoney object
def test_none_money_conversion():
    nm = NoneMoney()
    with pytest.raises(TypeError) as excinfo:
        float(nm)
    assert str(excinfo.value) == "Undefined monetary values do not have quantity information.", "Expected TypeError when converting NoneMoney to float"
