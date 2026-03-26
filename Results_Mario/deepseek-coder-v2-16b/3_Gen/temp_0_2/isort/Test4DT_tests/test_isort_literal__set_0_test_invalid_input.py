
from isort.literal import _set
from typing import Any

class MockPrettyPrinter:
    def pformat(self, obj):
        return str(obj)

def test_invalid_input():
    value = {3, 1, 2}
    printer = MockPrettyPrinter()
    result = _set(value, printer)
    assert result == "{1, 2, 3}"
