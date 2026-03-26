
import pytest
from pymonet.validation import Validation
try:
    from some_module_providing_box import Box  # Assuming this is where Box might be defined
except ImportError:
    class Box:  # Fallback definition if the module does not provide it
        pass

# Test creating a successful Validation instance
def test_successful_validation():
    val = Validation(10, [])  # Initializes a Validation object with the value 10 and no errors yet.
    assert val.value == 10
    assert len(val.errors) == 0

# Test adding an error to the Validation instance
def test_adding_error():
    val_with_errors = Validation(None, ["Error message"])
    val_with_errors.errors.append("Additional Error")
    assert len(val_with_errors.errors) == 2
    assert "Additional Error" in val_with_errors.errors

# Test transforming the Validation to a Box when successful
def test_transform_to_box_successful():
    validation = Validation(123, ["Error 1", "Error 2"])  # Create a Validation object with a success value and errors
    box = validation.to_box()  # Convert the Validation to a Box