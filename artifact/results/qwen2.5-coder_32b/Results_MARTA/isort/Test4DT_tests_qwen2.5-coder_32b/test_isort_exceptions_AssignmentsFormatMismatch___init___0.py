
import pytest
from isort.exceptions import AssignmentsFormatMismatch

def check_assignments_format(code: str):
    if code is None:
        raise ValueError("Code cannot be None")
    
    lines = code.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if '=' not in stripped_line or len(stripped_line.split('=')) != 2:
            raise AssignmentsFormatMismatch(code)

def test_edge_cases_none():
    with pytest.raises(ValueError):
        check_assignments_format(None)



def test_valid_inputs_correct_format():
    code = 'x = 1\ny = 2\nz = 3'
    try:
        check_assignments_format(code)
    except AssignmentsFormatMismatch as e:
        pytest.fail(f"Unexpected exception raised: {e}")

def test_invalid_inputs_multiple_errors_on_same_line():
    code = 'x=1 y=2\nz=3'
    with pytest.raises(AssignmentsFormatMismatch):
        check_assignments_format(code)

def test_valid_inputs_single_assignment():
    code = 'x = 1'
    try:
        check_assignments_format(code)
    except AssignmentsFormatMismatch as e:
        pytest.fail(f"Unexpected exception raised: {e}")
