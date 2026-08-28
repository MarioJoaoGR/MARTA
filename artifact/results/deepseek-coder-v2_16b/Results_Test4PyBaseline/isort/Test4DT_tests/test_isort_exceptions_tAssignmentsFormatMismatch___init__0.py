# Module: isort.exceptions
import pytest
from isort.exceptions import AssignmentsFormatMismatch

# Test Case 1: Raising an Exception with a Simple Code Snippet
def test_assignments_format_mismatch_simple():
    problematic_code = "apples = 10\nbananas = 20\ncherries = 30"
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

# Test Case 2: Raising an Exception with Complex Code Snippet
def test_assignments_format_mismatch_complex():
    problematic_code = """
    apples = 10
    bananas = 20
    cherries = 30
    dates = 40
    """
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

# Test Case 3: Handling the Exception in Code
def test_assignments_format_mismatch_handling():
    problematic_code = "apples = 10\nbananas = 20"
    try:
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
