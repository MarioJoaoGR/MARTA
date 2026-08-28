
import pytest
from pymonet.semigroups import All

def test_valid_input():
    all_true = All(True)
    assert all_true.value == True

def test_invalid_input():
    with pytest.raises(TypeError):
        All().concat(All())
