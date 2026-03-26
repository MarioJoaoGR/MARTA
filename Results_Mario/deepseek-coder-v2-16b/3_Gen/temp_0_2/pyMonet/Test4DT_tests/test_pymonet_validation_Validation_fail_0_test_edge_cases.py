
from pymonet.validation import Validation
import pytest

def test_fail():
    errors = ["Error1", "Error2"]
    failed_validation = Validation.fail(errors)
    assert failed_validation.value is None
    assert failed_validation.errors == errors
