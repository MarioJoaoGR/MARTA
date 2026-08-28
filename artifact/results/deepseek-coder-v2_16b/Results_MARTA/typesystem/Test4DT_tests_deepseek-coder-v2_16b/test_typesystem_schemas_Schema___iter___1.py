
import pytest
from typesystem.schemas import Schema, Field

# Scenario 1: Test initialization with a dictionary

# Scenario 2: Test initialization with keyword arguments

# Scenario 3: Test invalid keyword argument raises TypeError
def test_invalid_keyword_arg():
    class Field:
        def __init__(self, default=None):
            self.default = default
    
        def validate_or_error(self, value):
            return value or self.default, None
    
        def has_default(self):
            return self.default is not None
    
        def get_default_value(self):
            return self.default
    
    class SchemaExample(Schema):
        fields = {
            'name': Field(default='Unknown'),
            'age': Field()
        }
    
    with pytest.raises(TypeError) as excinfo:
        SchemaExample(invalid_arg='Invalid')
    assert str(excinfo.value) == "'invalid_arg' is an invalid keyword argument for SchemaExample()."

# Scenario 4: Test iteration over fields