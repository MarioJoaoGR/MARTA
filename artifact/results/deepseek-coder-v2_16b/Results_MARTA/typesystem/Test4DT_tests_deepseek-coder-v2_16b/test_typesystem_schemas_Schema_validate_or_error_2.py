
import pytest
from typesystem.schemas import Schema, Field

# Scenario 1: Test initialization with valid inputs using keyword arguments

# Scenario 2: Test initialization with no arguments, should use default values

# Scenario 3: Test initialization with invalid keyword argument, should raise TypeError
def test_invalid_keyword_argument():
    class SchemaExample(Schema):
        fields = {
            'name': Field(default='Unknown'),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        schema3 = SchemaExample(invalid_arg='Invalid')
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for SchemaExample()."