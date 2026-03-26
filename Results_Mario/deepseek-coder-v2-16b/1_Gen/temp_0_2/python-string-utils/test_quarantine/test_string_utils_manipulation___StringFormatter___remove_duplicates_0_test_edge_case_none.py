
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.exceptions import InvalidInputError

def test_edge_case_none():
    # Arrange
    formatter = None  # This should raise an InvalidInputError
    
    with pytest.raises(InvalidInputError) as exc_info:
        # Act
        formatter = __StringFormatter(None)
    
    # Assert
    assert str(exc_info.value) == "Expected a string but got NoneType"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_edge_case_none
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_edge_case_none.py:4:0: E0401: Unable to import 'string_utils.exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_edge_case_none.py:4:0: E0611: No name 'exceptions' in module 'string_utils' (no-name-in-module)


"""