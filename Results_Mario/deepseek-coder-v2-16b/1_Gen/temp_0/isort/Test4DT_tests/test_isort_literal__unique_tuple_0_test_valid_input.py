
from isort.literal import _unique_tuple
from unittest.mock import Mock

def test_valid_input():
    # Create a mock pretty printer
    printer = Mock()
    printer.pformat.return_value = "['1', '2', '3']"
    
    value = (3, 1, 2, 2, 3)
    result = _unique_tuple(value, printer)
    
    # Assert the expected output
    assert result == "['1', '2', '3']"
