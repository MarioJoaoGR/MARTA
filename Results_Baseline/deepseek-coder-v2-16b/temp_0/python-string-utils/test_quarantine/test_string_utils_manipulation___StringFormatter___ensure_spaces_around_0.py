
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def is_string(input_data):
    return isinstance(input_data, str)

class Test__StringFormatter:
    
    def test_valid_string_initialization(self):
        """Test that a valid string initializes the class correctly."""
        formatter = __StringFormatter("valid string")
        assert hasattr(formatter, 'text'), "Initialization should set text to a string"
    
    def test_invalid_input_raises_error(self):
        """Test that an InvalidInputError is raised for non-string input."""
        with pytest.raises(InvalidInputError):
            __StringFormatter(12345)
    
    def test_format_adds_spaces_around_substrings(self):
        """Test that the format method adds spaces around substrings."""
        formatter = __StringFormatter("ThisIsAExample")
        assert " ".join(["This", "Is", "A", "Example"]) == formatter.text, "Format should add spaces between words"
    
    def test_format_handles_already_spaced_input(self):
        """Test that the format method handles already spaced input correctly."""
        formatter = __StringFormatter("Hello World")
        assert "Hello World" == formatter.text, "Format should not change already spaced input"
    
    def test_format_handles_empty_string(self):
        """Test that the format method handles an empty string correctly."""
        formatter = __StringFormatter("")
        assert "" == formatter.text, "Format should handle empty string"
    
    def test_format_handles_none_input(self):
        """Test that the format method handles None input gracefully."""
        with pytest.raises(InvalidInputError):
            __StringFormatter(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_spaces_around_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_0.py:23:59: E1101: Instance of '__StringFormatter' has no 'text' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_0.py:28:32: E1101: Instance of '__StringFormatter' has no 'text' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_0.py:33:21: E1101: Instance of '__StringFormatter' has no 'text' member (no-member)

"""