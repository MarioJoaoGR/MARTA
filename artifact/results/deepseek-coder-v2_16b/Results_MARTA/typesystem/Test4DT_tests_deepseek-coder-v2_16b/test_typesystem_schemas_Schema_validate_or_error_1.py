
import pytest
from typesystem.schemas import Schema, Field

# Scenario 1: Test initialization with valid inputs using positional argument (dict)

# Scenario 2: Test initialization without arguments, using default values

# Scenario 3: Test handling of invalid keyword argument
def test_invalid_keyword_argument():
    class SchemaExample(Schema):
        fields = {
            'name': Field(default='Unknown'),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        schema = SchemaExample(invalid_arg='Invalid')
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for SchemaExample()."