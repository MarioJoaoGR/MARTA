
from isort.literal import Any
import pytest
from unittest.mock import MagicMock

# Assuming ISortPrettyPrinter is defined in a module, let's define it here for completeness
class ISortPrettyPrinter:
    def pformat(self, sorted_dict):
        pass

def _dict(value: dict[Any, Any], printer: ISortPrettyPrinter) -> str:
    return printer.pformat(dict(sorted(value.items(), key=lambda item: item[1])))

@pytest.mark.parametrize("value, expected", [
    ({}, "{}"),  # Test empty dictionary
    ({'a': 3, 'b': 1, 'c': 2}, "{'b': 1, 'c': 2, 'a': 3}"),  # Test sorted dictionary
])
def test_none_input(value, expected):
    printer = MagicMock()
    printer.pformat = MagicMock(return_value=expected)
    
    result = _dict(value, printer)
    
    assert result == expected
    printer.pformat.assert_called_once_with(dict(sorted(value.items(), key=lambda item: item[1])))
