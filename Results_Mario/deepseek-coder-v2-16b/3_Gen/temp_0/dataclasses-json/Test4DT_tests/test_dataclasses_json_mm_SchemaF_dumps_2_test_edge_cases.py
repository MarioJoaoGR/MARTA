
from dataclasses_json.mm import SchemaF  # Correctly importing from the specified module
import pytest

def test_schemaf_raises_notimplementederror():
    with pytest.raises(NotImplementedError):
        SchemaF()
