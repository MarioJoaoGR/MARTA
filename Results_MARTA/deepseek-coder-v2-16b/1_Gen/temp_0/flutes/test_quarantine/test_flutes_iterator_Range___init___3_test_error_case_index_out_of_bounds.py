
import pytest
from flutes.iterator import Range

def test_error_case_index_out_of_bounds():
    r = Range(10)  # Create a range from 0 to 9 with step size of 1
    
    # Test index out of bounds for positive indices
    with pytest.raises(IndexError):
        r[10]  # This should raise an IndexError because the length is 10, but we are trying to access index 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___init___3_test_error_case_index_out_of_bounds.py F [100%]

=================================== FAILURES ===================================
_____________________ test_error_case_index_out_of_bounds ______________________

    def test_error_case_index_out_of_bounds():
        r = Range(10)  # Create a range from 0 to 9 with step size of 1
    
        # Test index out of bounds for positive indices
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___init___3_test_error_case_index_out_of_bounds.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___3_test_error_case_index_out_of_bounds.py::test_error_case_index_out_of_bounds
============================== 1 failed in 0.09s ===============================
"""