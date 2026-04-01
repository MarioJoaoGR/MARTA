
import pytest
from dedupe import dedupe

def my_func():
    return [1, 2, 3, 4]

@pytest.fixture(params=[my_func])
def func(request):
    return request.param()

def test_valid_input(func):
    @dedupe(my_func, instance=None, args=(), kwargs={})
    def my_func():
        return [1, 2, 3, 2, 1]
    
    result = list(my_func())
    assert result == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_iters_dedupe_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0_test_valid_input.py:3:0: E0401: Unable to import 'dedupe' (import-error)


"""