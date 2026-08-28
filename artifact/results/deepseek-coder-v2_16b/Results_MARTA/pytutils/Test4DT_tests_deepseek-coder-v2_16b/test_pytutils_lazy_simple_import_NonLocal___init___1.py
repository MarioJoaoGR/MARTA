
import pytest
from pytutils.lazy.simple_import import NonLocal

def test_valid_input():
    nl = NonLocal(10)
    assert isinstance(nl, NonLocal), "Instance should be of type NonLocal"
    assert hasattr(nl, 'value'), "Instance should have a 'value' attribute"
    assert nl.value == 10, "The value should be 10"

def test_invalid_input():
    with pytest.raises(TypeError):
        NonLocal()
