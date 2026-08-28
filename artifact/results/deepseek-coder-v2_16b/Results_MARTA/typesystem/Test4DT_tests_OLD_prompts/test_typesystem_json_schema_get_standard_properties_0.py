
import pytest
from typesystem.json_schema import get_standard_properties, Field

# Test case for valid input with default value
def test_valid_input():
    field = Field()
    field.default = 123
    result = get_standard_properties(field)
    assert result == {'default': 123}

# Test case for invalid input (None)