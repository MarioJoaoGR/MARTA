
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    with pytest.raises(TypeError):
        val = Validation(None, ['Error message'])
        val.map(lambda x: x * 2)
