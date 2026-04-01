
import pytest
from isort.literal import AssignmentsFormatMismatch

def assignments(code: str) -> str:
    """
    Parses and sorts variable assignments from a given code string.
    
    This function takes a string of Python code containing multiple variable assignments, each on its own line, 
    and extracts the variable names and their corresponding values. It then returns a formatted string where the 
    variables are sorted by their names and presented in the format "{variable_name} = {value}".
    
    Parameters:
        code (str): A string containing Python code with multiple assignments. Each assignment should be on its own line, 
                     following the pattern "variable_name = value".
                     
    Returns:
        str: A formatted string where each variable and its assigned value are listed in alphabetical order by variable name.
    
    Raises:
        AssignmentsFormatMismatch: If the provided code does not contain valid assignments as expected by this function.
        
    Example:
        >>> assignments("var1 = 1\nvar2 = 2\nvar3 = 3")
        'var1 = 1\nvar2 = 2\nvar3 = 3'
        
        >>> try:
        ...     assignments("invalid code with no assignment")
        ... except AssignmentsFormatMismatch as e:
        ...     print(e)
        isort was told to sort a section of assignments, however the given code:
        
        invalid code with no assignment
        
        Does not match isort's strict single line formatting requirement for assignment sorting:
        
        {variable_name} = {value}
    """
    values = {}
    for line in code.splitlines(keepends=True):
        if not line.strip():
            continue
        if " = " not in line:
            raise AssignmentsFormatMismatch(code)
        variable_name, value = line.split(" = ", 1)
        values[variable_name] = value

    return "".join(f"{variable_name} = {values[variable_name]}" for variable_name in sorted(values.keys()))

def test_none_input():
    with pytest.raises(AssignmentsFormatMismatch):
        assignments("")

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

isort/Test4DT_tests/test_isort_literal_assignments_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(AssignmentsFormatMismatch):
E       Failed: DID NOT RAISE <class 'isort.exceptions.AssignmentsFormatMismatch'>

isort/Test4DT_tests/test_isort_literal_assignments_1_test_none_input.py:51: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal_assignments_1_test_none_input.py::test_none_input
============================== 1 failed in 0.11s ===============================
"""