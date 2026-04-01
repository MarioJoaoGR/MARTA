
import pytest

from isort.literal import _unique_tuple


class MockPrettyPrinter:
    def pformat(self, value): 
        return str(sorted(set(value)))

def test_edge_case_none():
    with pytest.raises(TypeError):
        printer = MockPrettyPrinter()
        result = _unique_tuple(None, printer)
