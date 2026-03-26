
from typing import Any, List

import pytest


# Assuming CustomPrettyPrinter is defined elsewhere in your module or imported from another package
class CustomPrettyPrinter:
    def pformat(self, value: List[Any]) -> str:
        return ", ".join(map(str, sorted(value)))

# Test cases for _list function
def test_sorted_numbers():
    list_to_sort = [3, 1, 4, 1, 5, 9]
    custom_printer = CustomPrettyPrinter()
    result = custom_printer.pformat(list_to_sort)
    assert result == "1, 1, 3, 4, 5, 9"

def test_sorted_strings():
    list_to_sort = ["banana", "apple", "cherry"]
    custom_printer = CustomPrettyPrinter()
    result = custom_printer.pformat(list_to_sort)
    assert result == "apple, banana, cherry"

def test_sorted_mixed_types():
    list_to_sort = [3, "banana", 1, "apple", 4, "cherry"]
    custom_printer = CustomPrettyPrinter()
    with pytest.raises(TypeError):
        result = custom_printer.pformat(list_to_sort)
