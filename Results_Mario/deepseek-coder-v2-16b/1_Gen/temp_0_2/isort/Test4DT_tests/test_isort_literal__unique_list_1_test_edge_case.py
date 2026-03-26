
from typing import Any
import pytest
from isort.literal import _unique_list  # Assuming this is the correct module path

class MockPrinter:
    def pformat(self, value):
        return ', '.join(map(str, value))

@pytest.mark.parametrize("value, expected", [
    ([3, 1, 2, 2, 3], '1, 2, 3'),
    (['a', 'b', 'a'], 'a, b')
])
def test_unique_list(value, expected):
    printer = MockPrinter()
    result = _unique_list(value, printer)
    assert result == expected
