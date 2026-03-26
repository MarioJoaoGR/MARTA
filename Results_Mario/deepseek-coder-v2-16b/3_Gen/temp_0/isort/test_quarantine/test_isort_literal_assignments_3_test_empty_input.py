
import pytest
from isort.exceptions import AssignmentsFormatMismatch

def assignments(code: str) -> str:
    """
    Parses and sorts variable assignments from a given string of Python code.

    This function takes a string containing multiple single-line variable assignments and returns them in sorted order based on the variable names. It assumes that each line contains exactly one assignment operation (e.g., `variable = value`). If any line does not conform to this format, it raises an `AssignmentsFormatMismatch` exception.

    Parameters:
        code (str): A string containing Python code with multiple single-line variable assignments. Each assignment should be on a new line and follow the format 'variable_name = value'.

    Returns:
        str: A string where each variable assignment is formatted as 'variable_name = value', sorted by the variable names.

    Raises:
        AssignmentsFormatMismatch: If any line in the provided code does not contain exactly one assignment operation or if it contains multiple assignments on a single line.

    Example:
        >>> code = "b = 2\na = 1\nc = 3"
        >>> sorted_assignments = assignments(code)
        >>> print(sorted_assignments)
        'a = 1\nb = 2\nc = 3'
    """
    values = {}
    for line in code.splitlines(keepends=True):
        if not line.strip():
            continue
        if " = " not in line:
            raise AssignmentsFormatMismatch(code)
        variable_name, value = line.split(" = ", 1)
        values[variable_name] = value

    return "".join(
        f"{variable_name} = {values[variable_name]}" for variable_name in sorted(values.keys())
    )

def test_empty_input():
    code = ""
    with pytest.raises(AssignmentsFormatMismatch):
        assignments(code)

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

isort/Test4DT_tests/test_isort_literal_assignments_3_test_empty_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_empty_input _______________________________

    def test_empty_input():
        code = ""
>       with pytest.raises(AssignmentsFormatMismatch):
E       Failed: DID NOT RAISE <class 'isort.exceptions.AssignmentsFormatMismatch'>

isort/Test4DT_tests/test_isort_literal_assignments_3_test_empty_input.py:41: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal_assignments_3_test_empty_input.py::test_empty_input
============================== 1 failed in 0.13s ===============================
"""