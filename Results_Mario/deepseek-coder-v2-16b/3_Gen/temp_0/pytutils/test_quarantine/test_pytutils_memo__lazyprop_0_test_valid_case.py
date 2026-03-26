
import pytest
from pytutils.memo import _lazyprop

class MyClass:
    def __init__(self, value):
        self.value = value
    
    @_lazyprop('cached_value', lambda self: self.value * 2)
    def double_value(self):
        pass

@pytest.fixture
def create_myclass():
    return MyClass(5)

def test_valid_case(create_myclass):
    obj = create_myclass
    assert obj.double_value() == 10  # First call, value is computed and cached
    assert obj.double_value() == 10  # Second call, value is retrieved from cache

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo__lazyprop_0_test_valid_case
pytutils/Test4DT_tests/test_pytutils_memo__lazyprop_0_test_valid_case.py:3:0: E0611: No name '_lazyprop' in module 'pytutils.memo' (no-name-in-module)


"""