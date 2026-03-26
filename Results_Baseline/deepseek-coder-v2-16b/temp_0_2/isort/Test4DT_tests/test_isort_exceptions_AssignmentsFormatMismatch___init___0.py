
import pytest

from isort.exceptions import (AssignmentsFormatMismatch, ExistingSyntaxErrors,
                              LiteralParsingFailure, LiteralSortTypeMismatch)


# Test for AssignmentsFormatMismatch
def test_assignments_format_mismatch():
    problematic_code = "a = 1\nb = 2\nc = 3"
    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch(problematic_code)
    assert str(exc_info.value) == (
        f"isort was told to sort a section of assignments, however the given code:\n\n{problematic_code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )
    assert exc_info.value.code == problematic_code

# Test for LiteralParsingFailure
def test_literal_parsing_failure():
    try:
        raise LiteralParsingFailure("some_code", ValueError("Could not parse this."))
    except LiteralParsingFailure as e:
        assert str(e) == "isort failed to parse the given literal some_code. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of Could not parse this.."
        assert e.code == "some_code"
        assert isinstance(e.original_error, ValueError)
        assert str(e.original_error) == "Could not parse this."

# Test for LiteralSortTypeMismatch
def test_literal_sort_type_mismatch():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(str, int)