
# Module: isort.exceptions
# test_isort_exceptions.py
from isort.exceptions import SortingFunctionDoesNotExist

def test_sorting_function_does_not_exist_exception():
    try:
        raise SortingFunctionDoesNotExist("invalid_order", ["ascending", "descending"])
    except SortingFunctionDoesNotExist as e:
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___0
isort/Test4DT_tests/test_isort_exceptions_SortingFunctionDoesNotExist___init___0.py:9:45: E0001: Parsing failed: 'expected an indented block after 'except' statement on line 9 (Test4DT_tests.test_isort_exceptions_SortingFunctionDoesNotExist___init___0, line 9)' (syntax-error)


"""