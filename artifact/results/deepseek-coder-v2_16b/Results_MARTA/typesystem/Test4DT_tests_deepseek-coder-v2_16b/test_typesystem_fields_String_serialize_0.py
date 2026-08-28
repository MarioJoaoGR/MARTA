
import pytest
from typesystem.fields import String
from typesystem.base import ValidationError

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test input with invalid max length
def test_invalid_max_length():
    string_field = String(allow_blank=True, trim_whitespace=False, max_length=10, min_length=5, pattern=r'^[a-zA-Z0-9]+$', format='email')
    with pytest.raises(ValidationError) as excinfo:
        string_field.validate("thisisalongstringwithmorethan10characters")
    assert str(excinfo.value) == "Must have no more than 10 characters."

# Scenario 3: Test input with invalid pattern