
import pytest

from isort.exceptions import AssignmentsFormatMismatch


def test_none_input():
    with pytest.raises(AssignmentsFormatMismatch) as excinfo:
        # This should raise the exception since we are passing None
        raise AssignmentsFormatMismatch("isort was told to sort a section of assignments, however the given code:\n\nNone\n\nDoes not match isort's strict single line formatting requirement for assignment sorting:\n\n{variable_name} = {value}\n{variable_name2} = {value2}\n...\n\n")
