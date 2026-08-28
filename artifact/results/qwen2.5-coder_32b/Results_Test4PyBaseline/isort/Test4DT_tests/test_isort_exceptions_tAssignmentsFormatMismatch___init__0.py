
import pytest
from isort.exceptions import AssignmentsFormatMismatch

def test_assignments_format_mismatch_basic():
    with pytest.raises(AssignmentsFormatMismatch) as excinfo:
        raise AssignmentsFormatMismatch("x=1\ny = 2\nz=3")
    assert "isort was told to sort a section of assignments, however the given code:\n\nx=1\ny = 2\nz=3\n\nDoes not match isort's strict single line formatting requirement for assignment sorting:\n\n{variable_name} = {value}\n{variable_name2} = {value2}\n...\n\n" in str(excinfo.value)
    assert excinfo.value.code == "x=1\ny = 2\nz=3"

def test_assignments_format_mismatch_complex():
    problematic_code = """
a=10
b=20
c = 30
d=40
"""
    with pytest.raises(AssignmentsFormatMismatch) as excinfo:
        raise AssignmentsFormatMismatch(problematic_code)