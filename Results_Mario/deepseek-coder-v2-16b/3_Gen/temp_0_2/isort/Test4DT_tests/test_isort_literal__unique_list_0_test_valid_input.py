
import pytest
from isort.literal import _unique_list
from typing import Any

class MockPrettyPrinter:
    def pformat(self, value):
        return ','.join(map(str, sorted(set(value))))

def test_valid_input():
    printer = MockPrettyPrinter()
    value = [3, 1, 2, 2, 3]
    expected_output = '1,2,3'
    result = _unique_list(value, printer)
    assert result == expected_output
