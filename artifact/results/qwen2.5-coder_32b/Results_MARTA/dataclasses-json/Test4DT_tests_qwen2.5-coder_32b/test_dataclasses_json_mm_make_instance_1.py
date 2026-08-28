
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import SchemaF

# Assuming _decode_dataclass is defined somewhere in the module
def _decode_dataclass(cls, kvs, partial):
    # Mock implementation for testing purposes
    return cls(**{**kvs, **kwargs})

@dataclass
class Person:
    name: str
    age: int





def test_SchemaF_instantiation_raises_NotImplementedError():
    """Test that attempting to instantiate SchemaF raises a NotImplementedError."""
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()

def test_SchemaF_subclass_instantiation_raises_NotImplementedError():
    """Test that attempting to instantiate a subclass of SchemaF raises a NotImplementedError."""
    class SubSchemaF(SchemaF):
        pass

    with pytest.raises(NotImplementedError):
        sub_schema_instance = SubSchemaF()