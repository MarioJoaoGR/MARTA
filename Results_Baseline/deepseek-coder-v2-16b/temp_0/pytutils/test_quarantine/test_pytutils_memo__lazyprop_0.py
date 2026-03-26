
# Module: pytutils.memo
import pytest
from pytutils.memo import MyClass

# Test fixture for MyClass
@pytest.fixture
def myclass():
    return MyClass(5)

# Test case to check the first access of double_value property
def test_double_value_first_access(myclass):
    assert myclass.double_value == 10

# Test case to check the subsequent access of double_value property
def test_double_value_subsequent_access(myclass):
    # Accessing the property again (retrieving the cached value)
    assert myclass.double_value == 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo__lazyprop_0
pytutils/Test4DT_tests/test_pytutils_memo__lazyprop_0.py:4:0: E0611: No name 'MyClass' in module 'pytutils.memo' (no-name-in-module)


"""