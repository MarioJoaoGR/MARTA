
import pytest
from dataclasses_json.mm import SchemaF

def test_instantiation_raises_exception():
    with pytest.raises(NotImplementedError):
        SchemaF()
