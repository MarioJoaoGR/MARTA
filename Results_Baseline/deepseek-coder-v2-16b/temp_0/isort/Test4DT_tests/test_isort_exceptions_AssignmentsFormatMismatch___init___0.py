# Module: isort.exceptions
import pytest

from isort.exceptions import AssignmentsFormatMismatch


# Test raising the exception with a sample code snippet
def test_assignments_format_mismatch_with_sample_code():
    problematic_code = "x = 1\ny = 2\nz = 3"
    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch(problematic_code)
    
    assert str(exc_info.value) == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{problematic_code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )
    assert exc_info.value.code == problematic_code

# Test handling the exception in a try-except block
def test_assignments_format_mismatch_in_try_except():
    try:
        problematic_code = "x = 1\ny = 2\nz = 3"
        raise AssignmentsFormatMismatch(problematic_code)
    except AssignmentsFormatMismatch as e:
        assert str(e) == (
            "isort was told to sort a section of assignments, however the given code:\n\n"
            f"{problematic_code}\n\n"
            "Does not match isort's strict single line formatting requirement for assignment sorting:\n\n"
            "{variable_name} = {value}\n"
            "{variable_name2} = {value2}\n"
            "...\n\n"
        )
        assert e.code == problematic_code
