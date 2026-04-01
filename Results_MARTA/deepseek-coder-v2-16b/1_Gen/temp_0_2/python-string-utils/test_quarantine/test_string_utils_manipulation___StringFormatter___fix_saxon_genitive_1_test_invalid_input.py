
import pytest
from string_utils.manipulation import InvalidInputError

class Test__StringFormatter:
    def test_invalid_input(self):
        # Arrange
        input_value = 12345  # Non-string value to simulate invalid input
        
        # Act and Assert
        with pytest.raises(InvalidInputError) as exc_info:
            __StringFormatter(input_value)
            
        # Assert the exception message is correct
        assert str(exc_info.value) == f"Expected a string but got {type(input_value).__name__}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_1_test_invalid_input.py:12:12: E0602: Undefined variable '__StringFormatter' (undefined-variable)


"""