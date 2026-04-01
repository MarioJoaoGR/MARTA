
from superstring.superstring import SuperStringBase, EdgeCaseSuperString
import pytest

@pytest.fixture
def edge_case_instance():
    return EdgeCaseSuperString("test")

def test_edge_case(edge_case_instance):
    assert len(edge_case_instance) == 4

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase___len___0_test_edge_case
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___len___0_test_edge_case.py:2:0: E0611: No name 'EdgeCaseSuperString' in module 'superstring.superstring' (no-name-in-module)


"""