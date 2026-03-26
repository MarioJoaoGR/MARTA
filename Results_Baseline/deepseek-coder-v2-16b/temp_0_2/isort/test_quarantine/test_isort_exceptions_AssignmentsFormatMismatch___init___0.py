
import pytest
from isort.exceptions import AssignmentsFormatMismatch, LiteralParsingFailure, LiteralSortTypeMismatch, ExistingSyntaxErrors

# Test for AssignmentsFormatMismatch
def test_assignments_format_mismatch():
    problematic_code = "a = 1\nb = 2\nc = 3"
    with pytest.raises(AssignmentsFormatMismatch) as excinfo:
        raise AssignmentsFormatMismatch(problematic_code)
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

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___0.py F [100%]

=================================== FAILURES ===================================
_______________________ test_assignments_format_mismatch _______________________

    def test_assignments_format_mismatch():
        problematic_code = "a = 1\nb = 2\nc = 3"
        with pytest.raises(AssignmentsFormatMismatch) as excinfo:
            raise AssignmentsFormatMismatch(problematic_code)
>       assert str(excinfo.value) == (
            f"{problematic_code}\n\n"
            "Does not match isort's strict single line formatting requirement for assignment sorting:\n\n"
            "{variable_name} = {value}\n"
            "{variable_name2} = {value2}\n"
            "...\n\n"
        )
E       AssertionError: assert 'isort was to...ue2}\n...\n\n' == 'a = 1\nb = 2...ue2}\n...\n\n'
E         
E         + isort was told to sort a section of assignments, however the given code:
E         + 
E           a = 1
E           b = 2
E           c = 3
E           ...
E         
E         ...Full output truncated (6 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_AssignmentsFormatMismatch___init___0.py::test_assignments_format_mismatch
============================== 1 failed in 0.09s ===============================
"""