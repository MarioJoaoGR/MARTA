
import pytest
from ansible.utils.version import _Numeric

def test_edge_cases():
    with pytest.raises(TypeError):
        num_none = _Numeric(None)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        num_str_to_float = _Numeric('5.5')
