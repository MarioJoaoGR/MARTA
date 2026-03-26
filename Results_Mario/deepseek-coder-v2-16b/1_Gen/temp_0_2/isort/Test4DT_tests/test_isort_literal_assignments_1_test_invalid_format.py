
import pytest
from isort.literal import AssignmentsFormatMismatch

def assignments(code: str) -> str:
    """
    Parses and sorts variable assignments from a given code string.
    
    This function takes a string of Python code that contains multiple variable assignments, each on its own line following the pattern `{variable_name} = {value}\n`. It extracts these assignments, stores them in a dictionary, and then returns a sorted string representation of the original assignments.
    
    Parameters:
        code (str): A string containing Python code with multiple variable assignments. Each assignment should be on a new line, following the format `{variable_name} = {value}\n`.
        
    Returns:
        str: A string where each assignment is sorted and formatted as `{variable_name} = {value}` in alphabetical order of the variable names.
    
    Raises:
        AssignmentsFormatMismatch: If the provided code does not conform to the expected format, i.e., if any line does not contain an '=' sign or is empty, this exception will be raised.
        
    Example:
        >>> assignments("var1 = value1\nvar2 = value2")
        'var1 = value1\nvar2 = value2'
        
        >>> try:
        ...     assignments("invalid code")
        ... except AssignmentsFormatMismatch as e:
        ...     print(e)
        isort was told to sort a section of assignments, however the given code:
        
        invalid code
        
        Does not match isort's strict single line formatting requirement for assignment sorting:
        
        {variable_name} = {value}\n
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

# Test case to check the function with valid input
def test_valid_assignments():
    code = "var1 = value1\nvar2 = value2"
    expected_output = "var1 = value1\nvar2 = value2"
    assert assignments(code) == expected_output

# Test case to check the function with invalid input
def test_invalid_assignments():
    code = "invalid code"
    with pytest.raises(AssignmentsFormatMismatch):
        assignments(code)
