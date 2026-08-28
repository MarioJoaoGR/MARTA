
import pytest
from typesystem.schemas import Schema, Field

# Test scenario 1: Initialize schema with dictionary

# Test scenario 2: Initialize schema with keyword arguments

# Test scenario 3: Handle invalid keyword argument
def test_schema_invalid_keyword_argument():
    class TestSchema(Schema):
        fields = {
            'name': Field(),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        schema = TestSchema(invalid_arg='Invalid')
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for TestSchema()."

# Test scenario 4: Initialize schema with default values