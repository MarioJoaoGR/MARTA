
import pytest
from dataclasses_json.mm import SchemaF, JsonData, TOneOrMulti

def test_schemaf_raises_notimplementederror():
    """Test that instantiating SchemaF raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        schema = SchemaF()
