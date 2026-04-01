
import pytest
from pytutils.props import roclassproperty

# Define a sample class to be used in the tests
class MyClass:
    def __init__(self, value):
        self._value = value
    
    @roclassproperty
    def value(cls):
        return cls._value

def test_edge_case():
    obj = MyClass(10)
    assert obj.value == 10
    
    with pytest.raises(AttributeError):
        obj.value = 20

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___get___0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_edge_case.py:11:4: E0213: Method 'value' should have "self" as first argument (no-self-argument)


"""