
import pytest
from dataclasses_json.mm import SchemaF

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
