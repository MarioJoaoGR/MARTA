
import pytest
from pymonet.semigroups import One

def test_valid_input():
    value = 42
    one_instance = One(value)
    assert str(one_instance) == f'One[value={value}]'
