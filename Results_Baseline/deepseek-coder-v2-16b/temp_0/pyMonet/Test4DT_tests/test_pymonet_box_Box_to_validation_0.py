
import pytest
from pymonet.box import Box
from pymonet.validation import Validation
import random

# Test 1: Creating a Box with an integer value and transforming it to Validation
def test_box_to_validation_integer():
    box = Box(123)
    validation_monad = box.to_validation()
    assert validation_monad.is_success(), "Expected the transformation to be successful"
    assert validation_monad.value == 123, "Expected the value in Validation to be 123"

# Test 2: Creating a Box with a string value and transforming it to Validation
def test_box_to_validation_string():
    box = Box("Hello, World!")
    validation_monad = box.to_validation()
    assert validation_monad.is_success(), "Expected the transformation to be successful"
    assert validation_monad.value == "Hello, World!", "Expected the value in Validation to be 'Hello, World!'"

# Test 3: Handling potential errors in a function that uses Box and Validation
def test_box_to_validation_error():
    def risky_operation():
        if random.random() > 0.5:
            return Box(None)  # Return a Box with None value in case of failure
        else:
            return Box("Success!")  # Return a Box with a success value

    box = risky_operation()  # Call the function that might fail
    validation_monad = box.to_validation()  # Transform the Box to a Validation monad
    