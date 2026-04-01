
import pytest
from isort.exceptions import AssignmentsFormatMismatch

def test_valid_input():
    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch("var1 = value1\nvar2 = value2")
    
    expected_message = (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        "var1 = value1\nvar2 = value2\n\n"
        "Does not match isort's strict single line formatting requirement for assignment sorting:\n\n"
        "{variable_name} = {value}\n{variable_name2} = {value2}\n...\n"
    )
    
    assert str(exc_info.value) == expected_message.format(
        variable_name="var1", value="value1", variable_name2="var2", value2="value2"
    )

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

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with pytest.raises(AssignmentsFormatMismatch) as exc_info:
            raise AssignmentsFormatMismatch("var1 = value1\nvar2 = value2")
    
        expected_message = (
            "isort was told to sort a section of assignments, however the given code:\n\n"
            "var1 = value1\nvar2 = value2\n\n"
            "Does not match isort's strict single line formatting requirement for assignment sorting:\n\n"
            "{variable_name} = {value}\n{variable_name2} = {value2}\n...\n"
        )
    
>       assert str(exc_info.value) == expected_message.format(
            variable_name="var1", value="value1", variable_name2="var2", value2="value2"
        )
E       AssertionError: assert 'isort was to...ue2}\n...\n\n' == 'isort was to...value2\n...\n'
E         
E         Skipping 183 identical leading characters in diff, use -v to show
E           sorting:
E           
E         - var1 = value1
E         - var2 = value2
E         + {variable_name} = {value}...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___0_test_valid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""