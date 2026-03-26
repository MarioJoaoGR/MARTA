
import pytest
from isort.exceptions import AssignmentsFormatMismatch

def test_none_input():
    with pytest.raises(AssignmentsFormatMismatch) as excinfo:
        try:
            raise AssignmentsFormatMismatch(None)
        except AssignmentsFormatMismatch as e:
            assert str(e) == "isort was told to sort a section of assignments, however the given code:\n\nNone\n\nDoes not match isort's strict single line formatting requirement for assignment sorting:\n\n{variable_name} = {value}\n{variable_name2} = {value2}\n...\n\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(AssignmentsFormatMismatch) as excinfo:
E       Failed: DID NOT RAISE <class 'isort.exceptions.AssignmentsFormatMismatch'>

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___1_test_none_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___1_test_none_input.py::test_none_input
============================== 1 failed in 0.09s ===============================
"""