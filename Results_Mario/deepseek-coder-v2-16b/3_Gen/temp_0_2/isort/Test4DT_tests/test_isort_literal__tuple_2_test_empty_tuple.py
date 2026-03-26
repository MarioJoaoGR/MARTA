
from typing import Any
from isort.literal import _tuple as isort_tuple  # Correctly importing the function

class MockPrettyPrinter:
    def pformat(self, value):
        return f"Sorted and pretty printed: {sorted(value)}"

def test_empty_tuple():
    mock_printer = MockPrettyPrinter()
    result = isort_tuple((3, 1, 2), mock_printer)
    assert result == "Sorted and pretty printed: [1, 2, 3]"
