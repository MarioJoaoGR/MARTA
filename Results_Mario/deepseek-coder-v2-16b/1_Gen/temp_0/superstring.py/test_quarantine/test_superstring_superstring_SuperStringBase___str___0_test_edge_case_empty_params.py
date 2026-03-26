
import pytest
from superstring import SuperStringBase

@pytest.fixture
def setup():
    return SuperStringBase("Hello", "World!")

def test_to_printable_no_params(setup):
    obj = setup
    assert str(obj) == "HelloWorld!"

def test_to_printable_with_start_index(setup):
    obj = setup
    assert obj.to_printable(start_index=6) == "World!"

def test_to_printable_with_end_index(setup):
    obj = setup
    assert obj.to_printable(end_index=5) == "Hello"

def test_to_printable_with_start_and_end_index(setup):
    obj = setup
    assert obj.to_printable(start_index=1, end_index=4) == "ell"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase___str___0_test_edge_case_empty_params
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_empty_params.py:3:0: E0611: No name 'SuperStringBase' in module 'superstring' (no-name-in-module)


"""