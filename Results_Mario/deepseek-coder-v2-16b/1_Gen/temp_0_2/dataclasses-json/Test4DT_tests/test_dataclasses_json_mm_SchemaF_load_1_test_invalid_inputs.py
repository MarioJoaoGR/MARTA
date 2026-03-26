
from dataclasses_json.mm import SchemaF
import pytest

def test_invalid_inputs():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()
