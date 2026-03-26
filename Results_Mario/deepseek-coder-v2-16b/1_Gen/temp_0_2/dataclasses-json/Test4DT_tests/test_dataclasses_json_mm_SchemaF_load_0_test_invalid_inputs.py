
import pytest
from dataclasses_json.mm import SchemaF  # Assuming 'dataclasses_json.mm' is the correct module

def test_invalid_inputs():
    with pytest.raises(NotImplementedError):
        SchemaF()
