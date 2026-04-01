
from typing import Any
import pytest
from unittest.mock import Mock

# Assuming ISortPrettyPrinter is defined somewhere, otherwise we would need to define it or adjust imports accordingly.
class ISortPrettyPrinter:
    def pformat(self, value):
        pass

def _unique_list(value: list[Any], printer: ISortPrettyPrinter) -> str:
    return printer.pformat(sorted(set(value)))

@pytest.mark.parametrize("value, expected", [
    ([3, 1, 2, 2, 3], "['1', '2', '3']"),
    (["a", "b", "a"], "['a', 'b']"),
    ([5, 4, 3, 2, 1], "['1', '2', '3', '4', '5']"),
    ([], "[]")
])
def test_unique_list(value, expected):
    mock_printer = Mock()
    mock_printer.pformat.return_value = expected
    
    result = _unique_list(value, mock_printer)
    
    assert result == expected
    mock_printer.pformat.assert_called_once_with(sorted(set(value)))
