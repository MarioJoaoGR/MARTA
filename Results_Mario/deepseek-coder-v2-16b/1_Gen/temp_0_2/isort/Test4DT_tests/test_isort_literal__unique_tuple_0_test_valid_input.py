
import pytest
from typing import Any
from isort.literal import ISortPrettyPrinter

def _unique_tuple(value: tuple[Any, ...], printer: ISortPrettyPrinter) -> str:
    return printer.pformat(tuple(sorted(set(value))))

# Test case for valid input
def test_valid_input():
    class DummyPrettyPrinter:
        def pformat(self, value):
            return f"Formatted {value}"
    
    printer = DummyPrettyPrinter()
    
    # Test with a tuple of integers
    result = _unique_tuple((1, 2, 2, 3), printer)
    assert result == 'Formatted (1, 2, 3)'
    
    # Test with a tuple of strings
    result = _unique_tuple(('a', 'b', 'a'), printer)
    assert result == 'Formatted (\'a\', \'b\')'
