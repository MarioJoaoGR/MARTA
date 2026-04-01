
import pytest
from typing import Any

# Assuming ISortPrettyPrinter is a placeholder for the actual interface or class used in the project
class MyPrettyPrinter:
    def pformat(self, value: list[Any]) -> str:
        return ', '.join(map(str, sorted(value)))

printer = MyPrettyPrinter()

def _list(value: list[Any], printer: 'ISortPrettyPrinter') -> str:
    return printer.pformat(sorted(value))

# Test function for test_empty_input
@pytest.mark.parametrize("value, expected", [([], ""), ([1, 2, 3], "1, 2, 3")])
def test_empty_input(value, expected):
    assert _list(value, printer) == expected
