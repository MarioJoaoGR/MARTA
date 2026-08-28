
import pytest
from pymonet.semigroups import Min

def test_valid_input():
    min_instance = Min(10)
    another_min_instance = Min(5)
    combined_min = min_instance.concat(another_min_instance)
    assert isinstance(combined_min, Min)
    assert combined_min.value == 5

def test_invalid_input():
    with pytest.raises(TypeError):
        Min().concat(Min())
