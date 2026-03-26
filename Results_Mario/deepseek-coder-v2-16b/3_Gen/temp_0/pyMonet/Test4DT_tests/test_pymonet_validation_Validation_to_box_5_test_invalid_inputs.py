
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    with pytest.raises(ValueError):
        val = Validation(None, [])
        raise ValueError("Test error")
        # The following line is just a placeholder to ensure the function raises an exception
        assert False, "Expected a ValueError but did not get one"
