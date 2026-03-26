
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import SchemaF

def test_invalid_inputs():
    with pytest.raises(NotImplementedError):
        # Attempting to instantiate the class should raise NotImplementedError
        schema_f = SchemaF()
