
import pytest
from dataclasses_json import mm

# Test to ensure that SchemaF cannot be instantiated directly
def test_schemaf_cannot_be_instantiated():
    with pytest.raises(NotImplementedError):
        schema_f = mm.SchemaF()
