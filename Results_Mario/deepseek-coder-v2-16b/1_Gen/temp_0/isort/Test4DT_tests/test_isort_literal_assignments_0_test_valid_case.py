
import pytest
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

def test_valid_case():
    code = "b = 2\na = 1\nc = 3"
    expected_output = 'a = 1\nb = 2\nc = 3'
    assert assignments(code) == expected_output
