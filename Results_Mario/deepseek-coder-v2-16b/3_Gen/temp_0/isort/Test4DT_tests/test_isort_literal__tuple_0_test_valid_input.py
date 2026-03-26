
# Importing _tuple from isort.literal as per the scenario
from typing import Any

from isort.literal import _tuple


class MockPrettyPrinter:
    def pformat(self, value):
        return f"Sorted: {sorted(value)}"

def test_valid_input():
    mock_printer = MockPrettyPrinter()
    sorted_tuple = _tuple((3, 1, 2), mock_printer)
    assert sorted_tuple == "Sorted: [1, 2, 3]"
