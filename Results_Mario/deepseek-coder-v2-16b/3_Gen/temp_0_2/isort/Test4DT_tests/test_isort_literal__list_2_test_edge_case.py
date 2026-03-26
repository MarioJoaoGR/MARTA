
from typing import Any, List
import pytest
from isort.literal import ISortPrettyPrinter  # Correctly importing ISortPrettyPrinter

class MyPrettyPrinter:
    def pformat(self, value: List[Any]) -> str:
        return ', '.join(map(str, sorted(value)))

def _list(value: list[Any], printer: ISortPrettyPrinter) -> str:
    return printer.pformat(sorted(value))

# Test case for the edge case scenario
def test_edge_case():
    list_to_sort = [3, 1, 2]
    printer = MyPrettyPrinter()
    result = _list(list_to_sort, printer)
    assert result == '1, 2, 3'
