
import re
from isort.literal import AssignmentsFormatMismatch

def test_valid_case():
    code = 'b = 2\na = 1\nc = 3'
    expected_output = 'a = 1\nb = 2\nc = 3'
    
    try:
        result = assignments(code)
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
    except AssignmentsFormatMismatch as e:
        assert False, str(e)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_literal_assignments_0_test_valid_case
isort/Test4DT_tests/test_isort_literal_assignments_0_test_valid_case.py:10:17: E0602: Undefined variable 'assignments' (undefined-variable)


"""