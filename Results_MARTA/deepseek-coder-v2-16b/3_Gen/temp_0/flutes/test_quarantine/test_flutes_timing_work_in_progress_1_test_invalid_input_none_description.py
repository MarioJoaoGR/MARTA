
import pytest
from flutes.timing import work_in_progress

def test_invalid_input_none_description():
    with pytest.raises(TypeError):
        @work_in_progress()  # No argument provided, should raise TypeError
        def func():
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_1_test_invalid_input_none_description.py F [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_input_none_description ______________________

    def test_invalid_input_none_description():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_timing_work_in_progress_1_test_invalid_input_none_description.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_timing_work_in_progress_1_test_invalid_input_none_description.py::test_invalid_input_none_description
============================== 1 failed in 0.10s ===============================
"""