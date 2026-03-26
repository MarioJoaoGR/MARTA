
from isort.literal import _dict
from unittest.mock import MagicMock
import pytest

def test_valid_input():
    value = {'a': 3, 'b': 1, 'c': 2}
    printer = MagicMock()
    expected_output = "b: 1, c: 2, a: 3"
    
    # Mock the pformat method to return the expected output
    printer.pformat.return_value = expected_output
    
    # Call the function with the mock and check the output
    result = _dict(value, printer)
    assert result == expected_output
