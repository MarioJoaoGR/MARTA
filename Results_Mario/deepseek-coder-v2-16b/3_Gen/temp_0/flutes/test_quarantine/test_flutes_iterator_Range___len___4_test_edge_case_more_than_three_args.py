
import pytest
from your_module import Range  # Replace with actual module import

def test_edge_case_more_than_three_args():
    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___len___4_test_edge_case_more_than_three_args
flutes/Test4DT_tests/test_flutes_iterator_Range___len___4_test_edge_case_more_than_three_args.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""