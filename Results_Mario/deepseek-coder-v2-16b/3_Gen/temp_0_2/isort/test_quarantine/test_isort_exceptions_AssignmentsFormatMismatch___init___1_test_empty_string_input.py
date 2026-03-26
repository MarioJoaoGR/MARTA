
import pytest
from isort.exceptions import AssignmentsFormatMismatch

def test_empty_string_input():
    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch("")
    
    # The expected error message includes a placeholder {variable_name} and {value}, which should be replaced by the actual code passed to the exception.
    # Since we are passing an empty string, we need to ensure that these placeholders do not appear in the error message.
    expected_message = "isort was told to sort a section of assignments, however the given code:\n\n\nDoes not match isort's strict single line formatting requirement for assignment sorting:\n\n{variable_name} = {value}\n{variable_name2} = {value2}\n...\n"
    expected_message = expected_message.format(variable_name="", value="", variable_name2="", value2="")
    
    assert str(exc_info.value) == expected_message

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

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___1_test_empty_string_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_empty_string_input ____________________________

    def test_empty_string_input():
        with pytest.raises(AssignmentsFormatMismatch) as exc_info:
            raise AssignmentsFormatMismatch("")
    
        # The expected error message includes a placeholder {variable_name} and {value}, which should be replaced by the actual code passed to the exception.
        # Since we are passing an empty string, we need to ensure that these placeholders do not appear in the error message.
        expected_message = "isort was told to sort a section of assignments, however the given code:\n\n\nDoes not match isort's strict single line formatting requirement for assignment sorting:\n\n{variable_name} = {value}\n{variable_name2} = {value2}\n...\n"
        expected_message = expected_message.format(variable_name="", value="", variable_name2="", value2="")
    
>       assert str(exc_info.value) == expected_message
E       AssertionError: assert 'isort was to...ue2}\n...\n\n' == 'isort was to... \n = \n...\n'
E         
E         Skipping 65 identical leading characters in diff, use -v to show
E           n code:
E         + 
E           
E           
E           Does not match isort's strict single line formatting requirement for assignment sorting:...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___1_test_empty_string_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___1_test_empty_string_input.py::test_empty_string_input
============================== 1 failed in 0.10s ===============================
"""