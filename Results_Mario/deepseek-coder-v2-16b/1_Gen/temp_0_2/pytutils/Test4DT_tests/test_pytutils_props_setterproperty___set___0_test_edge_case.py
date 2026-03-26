
import pytest
from pytutils.props import setterproperty

class EdgeCaseClass:
    def __init__(self, initial_value):
        self._value = initial_value

    @setterproperty
    def value(self, new_value):
        if new_value is not None:
            self._value = new_value

def test_edge_case():
    # Test initialization with None and empty values
    edge_case1 = EdgeCaseClass(None)
    assert edge_case1._value is None, "Initialization with None failed"

    edge_case2 = EdgeCaseClass('initial')
    assert edge_case2._value == 'initial', "Initialization with initial value failed"

    # Test setting value to None and empty values
    edge_case1.value = None
    assert edge_case1._value is None, "Setting value to None failed"

    edge_case2.value = ''
    assert edge_case2._value == '', "Setting value to empty string failed"

    # Test setting value to a valid non-empty value
    edge_case2.value = 'new_value'
    assert edge_case2._value == 'new_value', "Setting value to new valid string failed"

if __name__ == "__main__":
    pytest.main()
