
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation("Success", [])
    assert val.value == "Success"
    assert len(val.errors) == 0
    
    # Adding an error to check if the errors list remains empty
    with pytest.raises(AssertionError):
        assert len(val.errors) > 0
