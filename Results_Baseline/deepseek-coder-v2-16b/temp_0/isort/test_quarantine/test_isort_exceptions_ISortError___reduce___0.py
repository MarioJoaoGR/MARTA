
# Module: isort.exceptions
# test_isort_exceptions.py
from isort.exceptions import ISortError, CustomISortError, ExistingSyntaxErrors, LiteralSortTypeMismatch
from functools import partial
import pytest

def test_custom_isort_error():
    with pytest.raises(CustomISortError) as excinfo:
        raise CustomISortError("An error occurred in the isort process.")
    assert str(excinfo.value) == "An error occurred in the isort process."

def test_existing_syntax_errors():
    with pytest.raises(ExistingSyntaxErrors) as excinfo:
        raise ExistingSyntaxErrors("example_code.py")
    assert str(excinfo.value) == "example_code.py"

def test_literal_sort_type_mismatch():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(str, int)
    expected_message = "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'str'>."
    assert str(excinfo.value) == expected_message

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_ISortError___reduce___0
isort/Test4DT_tests/test_isort_exceptions_ISortError___reduce___0.py:4:0: E0611: No name 'CustomISortError' in module 'isort.exceptions' (no-name-in-module)


"""