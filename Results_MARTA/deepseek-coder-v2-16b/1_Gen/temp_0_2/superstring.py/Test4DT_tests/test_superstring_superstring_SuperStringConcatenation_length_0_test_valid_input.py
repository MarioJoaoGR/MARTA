
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringConcatenation  # Assuming this is the correct module path

def test_valid_input():
    # Mocking the SuperStringBase instances for left and right parts
    left_part = MagicMock()
    left_part.length.return_value = 5
    right_part = MagicMock()
    right_part.length.return_value = 5
    
    # Creating an instance of SuperStringConcatenation with mocked parts
    ssc = SuperStringConcatenation(left_part, right_part)
    
    # Assuming there's a concat method that returns the concatenated string
    ssc.concat = MagicMock()
    ssc.concat.return_value = "HelloWorld"  # Expected result of concatenation
    
    # Testing if the length method correctly calculates the combined length
    assert ssc.length() == 10  # Since both parts are mocked to have a length of 5, their sum should be 10
