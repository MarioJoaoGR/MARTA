
import pytest
from typesystem.fields import String, ValidationError

# Test for valid input happy path
def test_valid_input_happy_path():
    string_field = String(max_length=10, min_length=3, pattern=r'^[a-z]+$', format='lowercase')
    
    # Valid strings
    assert string_field.validate("abc") == "abc"
    assert string_field.validate("abcdefghij") == "abcdefghij"
    with pytest.raises(ValidationError) as excinfo:
        string_field.validate("validstring")
    assert str(excinfo.value) == String.errors['max_length'].format(max_length=10)

# Test for edge cases

# Test for invalid input error handling