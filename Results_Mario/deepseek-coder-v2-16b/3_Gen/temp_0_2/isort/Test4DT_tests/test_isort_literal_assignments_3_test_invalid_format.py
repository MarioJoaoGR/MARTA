
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

    return "".join(
        f"{variable_name} = {values[variable_name]}" for variable_name in sorted(values.keys())
    )

def test_invalid_format():
    with pytest.raises(AssignmentsFormatMismatch):
        assignments("invalid code with no assignment")
