
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

def test_success():
    val = Validation("Success", [])
    either_val = val.to_either()
    assert isinstance(either_val, Right)
    assert either_val.value == "Success"

def test_failure():
    val = Validation(None, ["Error occurred"])
    either_val = val.to_either()
    assert isinstance(either_val, Left)
    assert either_val.value == ["Error occurred"]
