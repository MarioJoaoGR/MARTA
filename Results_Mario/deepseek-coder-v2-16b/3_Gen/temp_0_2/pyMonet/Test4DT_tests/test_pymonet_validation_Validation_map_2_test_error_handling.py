
import pytest
from pymonet.validation import Validation

def test_error_handling():
    val = Validation("Success", [])
    with pytest.raises(TypeError):
        val.map(lambda x: x + 1)  # This should raise a TypeError because the mapper function expects an int but gets a str
