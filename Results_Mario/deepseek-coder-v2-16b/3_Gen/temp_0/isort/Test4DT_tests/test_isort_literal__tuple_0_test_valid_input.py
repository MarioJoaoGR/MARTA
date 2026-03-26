
# Importing _tuple from isort.literal as per the scenario
from isort.literal import _tuple
from typing import Any

class MockPrettyPrinter:
    def pformat(self, value):
        return f"Sorted: {sorted(value)}"

def test_valid_input():
    mock_printer = MockPrettyPrinter()
    sorted_tuple = _tuple((3, 1, 2), mock_printer)
    assert sorted_tuple == "Sorted: [1, 2, 3]"
