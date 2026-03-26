
import pytest
from flutes.multiproc import DummyApplyResult

def test_valid_input():
    value = "example_output"
    dummy_result = DummyApplyResult(value)
    
    assert dummy_result._value == value
    dummy_result.wait()  # Calling wait should not raise an error or change the state of the object
