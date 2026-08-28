
import pytest
from dataclasses_json.mm import SchemaF

def test_SchemaF_instantiation_raises_NotImplementedError():
    """Test that attempting to instantiate SchemaF raises a NotImplementedError."""
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()

