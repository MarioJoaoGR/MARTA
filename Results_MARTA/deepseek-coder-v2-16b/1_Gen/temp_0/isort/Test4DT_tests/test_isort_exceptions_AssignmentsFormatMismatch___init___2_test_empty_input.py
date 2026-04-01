
import pytest
from isort.exceptions import AssignmentsFormatMismatch

def test_empty_input():
    code = ''
    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch(code)
    
    assert str(exc_info.value) == "isort was told to sort a section of assignments, however the given code:\n\n" \
                                   f"{code}\n\n" \
                                   "Does not match isort's strict single line formatting requirement for assignment sorting:\n\n" \
                                   "{variable_name} = {value}\n" \
                                   "{variable_name2} = {value2}\n" \
                                   "...\n\n"
