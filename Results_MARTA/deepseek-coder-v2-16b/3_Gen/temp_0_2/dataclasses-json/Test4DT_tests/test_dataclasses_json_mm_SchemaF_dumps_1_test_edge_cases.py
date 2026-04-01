
import pytest
from dataclasses_json.mm import SchemaF

def test_edge_cases():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()
