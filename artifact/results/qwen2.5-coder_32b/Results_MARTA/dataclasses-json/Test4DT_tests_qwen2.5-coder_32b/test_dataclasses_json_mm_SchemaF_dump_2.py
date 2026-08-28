
import pytest
from dataclasses_json.mm import SchemaF

def test_SchemaF_instantiation_raises_NotImplementedError():
    """Test that attempting to instantiate SchemaF raises a NotImplementedError."""
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()

def test_SchemaF_subclass_cannot_be_instantiated():
    """Test that attempting to instantiate a subclass of SchemaF raises a NotImplementedError."""
    class MySchema(SchemaF):
        def dump(self, obj, many=None):
            pass
    
    with pytest.raises(NotImplementedError):
        my_schema_instance = MySchema()

