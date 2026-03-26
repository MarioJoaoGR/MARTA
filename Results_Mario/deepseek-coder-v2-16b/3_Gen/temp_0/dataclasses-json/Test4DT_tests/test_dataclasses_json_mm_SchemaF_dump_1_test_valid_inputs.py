
import pytest
from dataclasses_json.mm import SchemaF

def test_valid_inputs():
    with pytest.raises(NotImplementedError):
        SchemaF()
