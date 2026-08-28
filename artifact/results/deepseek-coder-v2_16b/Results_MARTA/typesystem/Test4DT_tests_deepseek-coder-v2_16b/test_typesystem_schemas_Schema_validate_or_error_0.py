
import pytest
from typesystem.schemas import Schema, Field

# Scenario 1: Test initialization with valid inputs using positional argument (dict)

# Scenario 2: Test initialization with default values

# Scenario 3: Test handling invalid keyword argument
def test_invalid_keyword_argument():
    class InvalidSchema(Schema):
        fields = {
            'name': Field(),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        InvalidSchema(invalid_arg='Invalid')
    
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for InvalidSchema()."