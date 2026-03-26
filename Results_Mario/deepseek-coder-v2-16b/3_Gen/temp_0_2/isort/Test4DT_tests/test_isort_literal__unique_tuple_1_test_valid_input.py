
import pytest
from collections import namedtuple
from typing import Any, List

# Mocking ISortPrettyPrinter and its pformat method
class MockPrettyPrinter:
    def __init__(self):
        self.formatted_values = []
    
    def pformat(self, value: List[Any]) -> str:
        return ', '.join(map(str, value))

# Function to be tested
def _unique_tuple(value: tuple[Any, ...], printer: 'ISortPrettyPrinter') -> str:
    return printer.pformat(tuple(sorted(set(value))))

# Test function
@pytest.mark.parametrize("input_values, expected", [
    ((3, 1, 2, 2, 3), "1, 2, 3"),
    ((1, 2, 3, 4, 5), "1, 2, 3, 4, 5"),
    ((5, 4, 3, 2, 1), "1, 2, 3, 4, 5"),
    ((1, 1, 1, 1, 1), "1"),
    ((7, 7, 7, 7, 7), "7")
])
def test_valid_input(input_values, expected):
    mock_printer = MockPrettyPrinter()
    result = _unique_tuple(input_values, mock_printer)
    assert result == expected
