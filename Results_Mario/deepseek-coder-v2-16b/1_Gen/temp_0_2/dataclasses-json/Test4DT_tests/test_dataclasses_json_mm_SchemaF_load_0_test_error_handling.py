
import pytest
from dataclasses_json.mm import SchemaF

def test_error_handling():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()
