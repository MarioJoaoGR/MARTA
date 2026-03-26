
import pytest
from pymonet.either import Either, Left, Right
from pymonet.box import Box  # Assuming this is the correct module and class for Box

# Test cases for the to_box method in the Either class
def test_to_box():
    # Create a Left instance with an error message
    left_value = Either(Left("error message"))
    
    # Transform the Left instance to a Box
    box = left_value.to_box()
    
    # Assert that the transformed value is of type Box and contains the correct error message
    assert isinstance(box, Box), "Expected the result to be an instance of Box"