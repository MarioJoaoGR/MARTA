
import re
from isort.literal import AssignmentsFormatMismatch

def assignments(code: str) -> str:
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

def test_valid_input():
    code = 'b = 2\na = 1\nc = 3'
    expected_output = 'a = 1\nb = 2\nc = 3'
    
    try:
        result = assignments(code)
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
    except AssignmentsFormatMismatch as e:
        assert False, f"Unexpected FormatMismatch exception: {e}"
