
from flutes.iterator import Range
import pytest

def test_error_case_index_out_of_range():
    r = Range(1, 5)  # Create a range from 1 to 4 with step 1
    with pytest.raises(IndexError):
        r[5]  # Attempting to access an index out of range

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

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_error_case_index_out_of_range.py F [100%]

=================================== FAILURES ===================================
______________________ test_error_case_index_out_of_range ______________________

    def test_error_case_index_out_of_range():
        r = Range(1, 5)  # Create a range from 1 to 4 with step 1
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_error_case_index_out_of_range.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___5_test_error_case_index_out_of_range.py::test_error_case_index_out_of_range
============================== 1 failed in 0.09s ===============================
"""