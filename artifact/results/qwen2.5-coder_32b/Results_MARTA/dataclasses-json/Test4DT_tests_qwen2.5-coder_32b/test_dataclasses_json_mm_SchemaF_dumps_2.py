
import pytest
from dataclasses_json.mm import SchemaF

# Define a simple dataclass for testing
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

# Subclass SchemaF to implement custom serialization logic
class MySchema(SchemaF):
    def dumps(self, obj, many=None) -> str:
        if many is None:
            many = isinstance(obj, list)
        
        if many:
            return json.dumps([user.__dict__ for user in obj])
        else:
            return json.dumps(obj.__dict__)

# Test that attempting to instantiate SchemaF raises a NotImplementedError
def test_SchemaF_instantiation_raises_NotImplementedError():
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()

# Test valid single object serialization

# Test edge case of empty list serialization

# Test invalid input non-dataclass