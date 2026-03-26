
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation("Success", [])
    assert not val.is_fail(), "Expected no errors, but found some"
