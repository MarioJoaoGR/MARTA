
import pytest
from pypara.monetary import NoneMoney

# Test cases for the round method in the NoneMoney class
def test_round_default():
    money_instance = NoneMoney()
    result = money_instance.round()
    assert isinstance(result, NoneMoney), "Expected a new instance of NoneMoney"
    with pytest.raises(TypeError):  # Adding this to ensure the correct exception is raised
        float(result)

def test_round_with_ndigits():
    money_instance = NoneMoney()
    result = money_instance.round(2)