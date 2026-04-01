
import pytest
from pymonet.validation import Validation

def test_fail():
    failed_validation = Validation.fail(errors=["Error 1", "Error 2"])
    assert failed_validation.value is None
    assert failed_validation.errors == ["Error 1", "Error 2"]
