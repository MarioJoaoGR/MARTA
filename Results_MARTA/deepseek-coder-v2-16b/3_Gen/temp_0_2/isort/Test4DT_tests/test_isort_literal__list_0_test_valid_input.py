
import pytest
from typing import Any, List

# Assuming ISortPrettyPrinter is defined somewhere in your codebase or standard library
class MockPrettyPrinter:
    def pformat(self, value: list[Any]) -> str:
        return ', '.join(map(str, sorted(value)))

def _list(value: list[Any], printer: 'ISortPrettyPrinter') -> str:
    return printer.pformat(sorted(value))

@pytest.fixture
def mock_printer():
    return MockPrettyPrinter()

def test_valid_input(mock_printer):
    list_to_sort = [3, 1, 2]
    result = _list(list_to_sort, mock_printer)
    assert result == '1, 2, 3'
