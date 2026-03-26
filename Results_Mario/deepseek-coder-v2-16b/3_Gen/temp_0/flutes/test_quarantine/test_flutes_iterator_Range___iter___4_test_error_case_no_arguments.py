
import pytest
from flutes.Test4DT_tests.test_flutes_iterator_Range___iter___4_test_error_case_no_arguments import Range

def test_range_with_no_arguments():
    with pytest.raises(ValueError) as excinfo:
        r = Range()
    assert str(excinfo.value) == "Range should be called the same way as the builtin `range`"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___iter___4_test_error_case_no_arguments
flutes/Test4DT_tests/test_flutes_iterator_Range___iter___4_test_error_case_no_arguments.py:3:0: E0401: Unable to import 'flutes.Test4DT_tests.test_flutes_iterator_Range___iter___4_test_error_case_no_arguments' (import-error)
flutes/Test4DT_tests/test_flutes_iterator_Range___iter___4_test_error_case_no_arguments.py:3:0: E0611: No name 'Test4DT_tests' in module 'flutes' (no-name-in-module)

"""