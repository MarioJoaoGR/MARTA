
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
    code = """var2 = 2
var1 = 1
var3 = 3"""
    
    expected_output = "var1 = 1\nvar2 = 2\nvar3 = 3"
    assert assignments(code) == expected_output
