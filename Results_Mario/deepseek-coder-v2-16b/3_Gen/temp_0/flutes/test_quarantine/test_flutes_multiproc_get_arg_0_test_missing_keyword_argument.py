
import pytest
from flutes.multiproc import get_arg

@pytest.fixture(autouse=True)
def reset_globals():
    global args, kwargs
    args = []
    kwargs = {}

def test_get_arg_with_positional_argument():
    args = [1, 2]
    assert get_arg(0, 'name', 'default') == 1

def test_get_arg_with_keyword_argument():
    kwargs = {'name': 'value'}
    assert get_arg(1, 'name', 'default') == 'value'

def test_get_arg_without_arguments():
    assert get_arg(0, 'name', 'default') == 'default'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_get_arg_0_test_missing_keyword_argument
flutes/Test4DT_tests/test_flutes_multiproc_get_arg_0_test_missing_keyword_argument.py:3:0: E0611: No name 'get_arg' in module 'flutes.multiproc' (no-name-in-module)


"""