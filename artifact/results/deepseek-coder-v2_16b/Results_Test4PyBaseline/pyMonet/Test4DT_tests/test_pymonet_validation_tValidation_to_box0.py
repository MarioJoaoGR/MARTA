
# Module: pymonet.validation
import pytest
from pymonet.validation import Validation
try:
    from pymonet.box import Box  # Assuming this import should be here for the sake of example, replace with actual module if needed
except ImportError:
    pass

# Test initialization of Validation object with success value and no errors
def test_init_success():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test initialization of Validation object with failure value and errors
def test_init_failure():
    val = Validation(None, ['Error message'])
    assert val.value is None
    assert val.errors == ['Error message']

# Test to_box method for successful validation
def test_to_box_success():
    val = Validation(10, [])
    box = val.to_box()
    assert isinstance(box, Box)  # Assuming 'Box' is defined in some module and should be imported or referenced correctly
    assert box.value == 10

# Test to_box method for failed validation
def test_to_box_failure():
    val = Validation(None, ['Error message'])
    box = val.to_box()
    assert isinstance(box, Box)  # Assuming 'Box' is defined in some module and should be imported or referenced correctly
    assert box.value is None

# Test is_success method for successful validation
def test_is_success_true():
    val = Validation(10, [])
    assert val.is_success() == True

# Test is_success method for failed validation
def test_is_success_false():
    val = Validation(None, ['Error message'])
    assert val.is_success() == False
