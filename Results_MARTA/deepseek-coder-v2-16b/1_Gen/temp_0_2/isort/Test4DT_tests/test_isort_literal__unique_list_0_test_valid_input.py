
import pytest
from typing import Any, List

# Assuming ISortPrettyPrinter is defined somewhere in the module 'isort.literal'
class MockPrinter:
    def pformat(self, value):
        return ', '.join(map(str, value))

printer = MockPrinter()

def _unique_list(value: List[Any], printer: "ISortPrettyPrinter") -> str:
    return printer.pformat(sorted(set(value)))

@pytest.mark.parametrize("input_list, expected", [
    ([3, 1, 2, 2, 3], '1, 2, 3'),
    (['a', 'b', 'a'], 'a, b'),
    ([5, 4, 3, 2, 1], '1, 2, 3, 4, 5'),
    ([10, -1, 0, 0, 10], '-1, 0, 10'),
    (['foo', 'bar', 'baz', 'foo'], 'bar, baz, foo')
])
def test_valid_input(input_list, expected):
    assert _unique_list(input_list, printer) == expected
